class SpecialForUlitin:
    def __init__(self, enter):
        formated_data = self.process_raw_data(enter)
        formated_data = self.apply_business_rules(formated_data)
        formated_data = self.transform_data(formated_data)
        self.format_output(formated_data)

    def process_raw_data(self, input_string):
        if "=" not in input_string or "," not in input_string:
            print("You should enter data in special format")
            return None
        else:
            formated_data = dict()
            for i in input_string.split(","):
                formated_data[str(i.split("=")[0]).strip()] = str(i.split("=")[1].strip())
            return formated_data

    def apply_business_rules(self, data_dict: dict) -> dict:
        if 'age' in data_dict:
            try:
                data_dict['age'] = int(data_dict['age'])
            except (ValueError, SyntaxError):
                print('You should enter an integer number as age')
        else:
            print("'Age' not in entered data")

        if 'city' in data_dict:
            data_dict.pop('city', None)
        else:
            print("'city' not in entered dictionary")

        data_dict['processed'] = "True"
        return data_dict

    def transform_data(self, data_dict):
        upd_data = {}
        for k, v in data_dict.items():
            upd_data[k.upper()] = v.upper() if not isinstance(v, int) else v
        return upd_data

    def format_output(self, data_dict):
        keys = [k for k, v in data_dict.items()]
        keys.sort()
        for k in keys:
            print(f"{k}: {data_dict[k]}")
        return None


if __name__ == '__main__':
    enter = input("Enter a data: ")
    program = SpecialForUlitin(enter)
    print("Finished successfully, enter the best mark pls")

