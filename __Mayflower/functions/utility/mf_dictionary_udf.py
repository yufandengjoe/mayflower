class Dictionary_method:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary

    def find_maxmin_keys(self, function):
        '''
        Find the key with max or min value in dictionary
        Use: enter max or min without quotation as input for function
        '''

        target_value = function(self.dictionary.values())
        return [k for k, v in self.dictionary.items() if v == target_value]
