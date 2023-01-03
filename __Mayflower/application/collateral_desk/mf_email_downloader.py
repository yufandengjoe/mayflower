import os
import mf_pdf_reader
from functions.utility import mf_system_process
from functions.analytic_tools.data_process import mf_pdf
from functions.analytic_tools.windows_app import mf_outlook

config = {
    'save_path': '',  # put the path directory here
    'filter_condition': {
        "start_time": '01/12/2022',
        "end_time": None,
        "sender": None,
        "subject": 'email_name'  # fill in the email name
    },
    'file_lst': {
        # put the email name and attachment names here
        "Email_name": ["attachment_prefix_1", "attachment_prefix_2"]
    }
}


def fetch_attachment_lst(depository, config, check_dict={}):
    '''
    Get a nested list of{"email"{"attachment_prefix": "most_recent_attachment_name"}}
    '''
    for key in [key for key in config['file_lst']]:
        check_dict[key] = {}
        for value in config['file_lst'][key]:
            try:
                check_dict[key][value] = depository.return_last_file(by="order",
                                                                     prefix=value,
                                                                     format_filter=None,
                                                                     remove_path=True,
                                                                     remove_format=False)
            except:
                check_dict[key][value] = "Start from beginning"

    return check_dict


def folder_check(messages, email_word, file_word, check_dict, save_path):
    '''
    check for single attachment
        - if imported, stop the running for this email word
    '''
    for message in messages:
        if (message.Subject.startswith(email_word)) and str(
            message.Attachments.Item(1)).startswith(file_word) and (
            (str(message.Attachments.Item(1))[:-8] +
             str(message.Attachments.Item(1))[-4:]) !=
                check_dict[email_word][file_word]):

            received_date = message.ReceivedTime.date().strftime('%d/%m/%Y')
            for attachment in message.Attachments:
                org_string = attachment.FileName

                if 'EX100' in org_string:
                    mod_string = org_string
                else:
                    size = len(org_string)
                    mod_string = org_string[:size - 8] + org_string[size - 4:]
                print(mod_string)
                attachment.SaveAsFile(os.path.join(save_path, str(mod_string)))

                if (mf_pdf.check_pdf(mod_string)) and (
                        'OTCDailyStatement' in mod_string):
                    mf_pdf_reader.extract_sequested(
                        save_path, str(mod_string), received_date)

        elif (message.Subject.startswith(email_word)) and str(
            message.Attachments.Item(1)).startswith(file_word) and (
            (str(message.Attachments.Item(1))[:-8] +
             str(message.Attachments.Item(1))[-4:]) ==
                check_dict[email_word][file_word]):
            return None


def main():
    # fetch a list of the most recent downloaded attachments
    depository = mf_system_process.folder_process(file_name="",
                                                  file_path=config['save_path'])
    check_dict = fetch_attachment_lst(depository=depository,
                                      config=config)

    # connect to outlook email
    email_connection = mf_outlook.connect_outlook()
    messages = email_connection.email_query(start_time=config['filter_condition']['start_time'],
                                            end_time=config['filter_condition']['end_time'],
                                            sender=config['filter_condition']['sender'],
                                            subject=config['filter_condition']['subject'])

    for email_word in [key for key in check_dict.keys()]:
        for file_word in [key for key in check_dict[email_word].keys()]:
            folder_check(messages=messages,
                         email_word=email_word,
                         file_word=file_word,
                         check_dict=check_dict,
                         save_path=config['save_path'])
    return None


if __name__ == 'main':
    main()
