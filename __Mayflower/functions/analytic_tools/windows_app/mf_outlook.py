import win32com.client as win32


class connect_outlook:

    def __init__(self):
        self.outlook = win32.Dispatch("outlook.application")
        return None

    def email_sender(self, to='', cc='', subject='', body='', attachment=[]):
        '''
        Automate sending email
        '''
        mail = self.outlook.CreateItem(0)
        mail.To = to
        mail.CC = cc
        mail.Subject = subject
        mail.Body = body
        if len(attachment) > 0:
            for file in attachment:
                mail.Attachments.Add(file)
        mail.Send()

        return None

    def email_query(self, start_time=None, end_time=None, sender=None, subject=None, blur_search=False):
        '''
        Query in the email box
            - blur search allows for search substring
            - date string format dd/mm/yyyy
        '''
        # load email inbox information
        outlook_object = self.outlook.GetNameSpace("MAPI")
        inbox = outlook_object.GetDefaultFolder(6)
        self.message = inbox.Items

        if start_time:
            self.message = self.message.Restrict(
                "[ReceivedTime >= '" + start_time + "'")

        if end_time:
            self.message = self.message.Restrict(
                "[ReceivedTime <= '" + end_time + "'")

        if sender:
            self.message = self.message.Restrict(
                "[SenderEmailAddress = '" + sender + "'")

        if subject and not blur_search:
            self.message = self.message.Restrict(
                "[Subject] = '" + subject + "'")

        elif subject and blur_search:
            self.message = self.message.Restrict(
                "@SQL=(urn:schemas:httpmail:subject LIKE '%" + subject + "%'")

        # Sort the email message from the most recent to the earliest
        self.message.Sort("[ReceivedTime]", True)

        return self.message
