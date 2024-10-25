import re

default_county_code = '38'


def normalize_phone(phone_number: str) -> str:
    pattern = r"[^\d]"
    phone = re.sub(pattern, "", phone_number)

    if not phone.startswith(default_county_code):
        phone = default_county_code + phone

    return "+" + phone


if __name__ == "__main__":
    # Test cases
    raw_numbers = ["067\\t123 4567",
                   "(095) 234-5678\\n",
                   "+380 44 123 4567",
                   "380501234567",
                   "    +38(050)123-32-34",
                   "     0503451234",
                   "(050)8889900",
                   "38050-111-22-22",
                   "38050 111 22 11   ", ]

    for phone in raw_numbers:
        print(normalize_phone(phone))
