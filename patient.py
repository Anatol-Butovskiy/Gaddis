class Patient:

    def __init__(self, first, middle, last, address, city,
                 state, zip_code, phone, em_contact, em_phone):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__em_contact = em_contact
        self.__em_phone = em_phone

    def set_first(self, first):
        self.__first = first

    def set_middle(self, middle):
        self.__middle = middle

    def set_last(self, last):
        self.__last = last



