def format_date_into_string(date):
    return '{}-{}-{} {}:{}:{}'.format(
        date.year, 
        date.month if date.month >= 10 else '0{}'.format(date.month), 
        date.day if date.day >= 10 else '0{}'.format(date.day),
        date.hour if date.hour >= 10 else '0{}'.format(date.hour), 
        date.minute if date.minute >= 10 else '0{}'.format(date.minute), 
        date.second if date.second >= 10 else '0{}'.format(date.second),
    )