import urwid


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def is_very_long(password):
    return len(password) >= 12


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def main():
    has_digit_call = has_digit

    is_very_long_call = is_very_long

    has_letters_call = has_letters

    has_upper_letters_call = has_upper_letters

    has_lower_letters_call = has_lower_letters

    has_symbols_call = has_symbols

    checks = [
        is_very_long_call,
        has_digit_call,
        has_letters_call,
        has_upper_letters_call,
        has_lower_letters_call,
        has_symbols_call
    ]

    def on_ask_change(edit, new_edit_text):
        score = 0
        for check in checks:
            if check(new_edit_text):
                score = score + 2
        reply.set_text("Рейтинг пароля: %s" % score)

    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()

