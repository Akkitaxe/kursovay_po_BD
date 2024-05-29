import mysql.connector

# ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ К БД

def search_bar_guest_FIO(conn, FIO):
    sql = """
    SELECT menu_id, napitki_id, zakuski_id, ФИО, Номер_столика FROM bar.guest WHERE ФИО = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (FIO,))
    results = cur.fetchmany(1)
    print('Вот гость с данным ФИО')
    for row in results:
        print(row,'\n')

def search_bar_guest_stolik(conn, stolik):
    sql = """
    SELECT  menu_id, napitki_id, zakuski_id, ФИО, Номер_столика FROM bar.guest WHERE Номер_столика = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (stolik,))
    results = cur.fetchmany(10)
    print('Вот несколько гостей за этим столиком')
    for row in results:
        print(row,'\n')

def search_bar_guest_guest_id(conn, guestId):
    sql = """
    SELECT  menu_id, napitki_id, zakuski_id, ФИО, Номер_столика FROM bar.guest WHERE guest_id = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (guestId,))
    results = cur.fetchmany(10)
    print('Вот гость с данным id')
    for row in results:
        print(row,'\n')

def search_bar_guest_menu_id(conn,menuId):
    sql = """
    SELECT  menu_id, napitki_id, zakuski_id, ФИО, Номер_столика FROM bar.guest WHERE menu_id = %s
    LIMIT 10
    """
    cur = conn.cursor()
    cur.execute(sql, (menuId,))
    results = cur.fetchmany(10)
    print('Вот гость с данным меню')
    for row in results:
        print(row,'\n')

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ book
def create_guest(conn, guest):
    sql = """
     INSERT INTO guest (menu_id, napitki_id, zakuski_id, ФИО, Номер_столика)
    VALUES (%s, %s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, guest)
    conn.commit()

def get_guest(conn, guest_id):
    sql = """
    SELECT *
    FROM guest
    WHERE guest_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (guest_id,))
    return cur.fetchone()

def update_guest(conn, guest):
    sql = """
    UPDATE guest
    SET menu_id = %s, napitki_id = %s, zakuski_id = %s,  ФИО = %s, Номер_столика = %s
    WHERE guest_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, guest)
    conn.commit()

def delete_guest(conn, book_id):

    sql2 = "DELETE FROM guest WHERE guest_id = %s"
    cur = conn.cursor()

    cur.execute(sql2, (book_id,))
    conn.commit()

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ sklad
def create_client(conn, client):
    sql = """
    INSERT INTO sklad (Адрес, Собственник) 
    VALUES (%s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()

def get_client(conn, client_id):
    sql = """
    SELECT * 
    FROM sklad
    WHERE sklad_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (client_id,))
    return cur.fetchone()

def update_client(conn, client):
    sql = """
    UPDATE sklad
    SET Адрес = %s, Собственник = %s
    WHERE sklad_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()

def delete_client(conn, client_id):
    sql1 = "DELETE FROM sklad WHERE sklad_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (client_id,))
    conn.commit()

# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ defekt
def create_order(conn, order):
    sql = """
   INSERT INTO defekt (eda_id, hosztovar_id, Критичность, Описание)
    VALUEs (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()

def get_order(conn, order):
    sql = """
    SELECT * 
    FROM defekt
    WHERE defekt_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (order,))
    return cur.fetchone()

def update_order(conn, order):
    sql = """
    UPDATE defekt
    SET eda_id = %s, hosztovar_id = %s, Критичность = %s, Описание = %s
    WHERE defekt_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()


def delete_order(conn, order):
    sql1 = "DELETE FROM defekt WHERE defekt_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (order,))
    conn.commit()


# ФУНКЦИИ ДЛЯ ПОДКЛЮЧЕНИЯ И ОТКЛЮЧЕНИЯ ОТ БД
def connect_to_db(host, user, password, database):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Успешное подключение к {database} с помощью MySQL Connector/Python\n")
    except Exception as e:
        print(f"Произошла ошибка при подключении к базе данных: {e}")
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        print("\nСоединение с базой данных закрыто")


# ОСНОВНАЯ ФУНКЦИЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ ПРОГРАММЫ
def main():
    host = "localhost"
    user = "root"
    password = "1234"
    database = "bar"
    conn = connect_to_db(host, user, password, database)

    while True:
        print("\nВыберите таблицу с которой хотите взаимодействовать \n или одно из функциональных требований:")
        print("1) defekt")
        print("2) sklad")
        print("3) guest")
        print(" ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ")
        print("4) Поиск гостя по ФИО")
        print("5) Поиск гостя по номеру столика")
        print("6) Поиск гостя по id гостя")
        print("7) Поиск гостя по id меню")
        print("8) Выход")
        table_choice = input("Введите номер пункта: ")

        if table_choice == '8':
            break
        if(table_choice == '1' or table_choice == '2' or table_choice == '3' ):
            print("\nВыберите действие:")
            print("1) Добавить запись")
            print("2) Просмотреть запись")
            print("3) Обновить запись")
            print("4) Удалить запись")
            print("5) Назад")
            action_choice = input("Введите номер пункта: ")
            if action_choice == '5':
                continue


        if table_choice == '1':  # defekt
            
            if action_choice == '1':
                new_order = tuple(input("Введите данные дефекта через запятую(eda_id, hosztovar_id, Критичность, Описание): ").split(','))
                create_order(conn, new_order)
            
            elif action_choice == '2':
                ID_order = input("Введите ID дефекта: ")
                order = get_order(conn, ID_order)
                print(order)
            
            elif action_choice == '3':
                updated_order_id = input("Введите ID дефекта для обновления: ")
                updated_order = list(input("Введите обновленные данные дефекта через запятую(eda_id, hosztovar_id, Критичность, Описание): ").split(','))
                updated_order.append(updated_order_id)
                updated_order_tuple = tuple(updated_order)
                update_order(conn, updated_order_tuple)
            
            elif action_choice == '4':
                ID_order_del = input("Введите ID дефекта для удаления: ")
                delete_order(conn, ID_order_del)
        
        
        elif table_choice == '2':  # sklad
            
            if action_choice == '1':
                new_client = tuple(input("Введите данные склада через запятую(Адрес, Собственник): ").split(','))
                create_client(conn, new_client)
            
            elif action_choice == '2':
                ID_client = input("Введите ID склада: ")
                client = get_client(conn, ID_client)
                print(client)
            
            elif action_choice == '3':
                updated_client_id = input("Введите ID склада для обновления: ")
                updated_client = list(input("Введите обновленные данные клиента через запятую(Адрес, Собственник): ").split(','))
                updated_client.append(updated_client_id)
                updated_client_tuple = tuple(updated_client)
                update_client(conn, updated_client_tuple)
            
            elif action_choice == '4':
                ID_client_del = input("Введите ID склада для удаления: ")
                delete_client(conn, ID_client_del)
        
        
        elif table_choice == '3':  # guest
            
            if action_choice == '1':
                new_guest = tuple(input("Введите информацию о госте через запятую\n(menu_id, napitki_id, zakuski_id, ФИО, Номер_столика): ").split(','))
                create_guest(conn, new_guest)
            
            elif action_choice == '2':
                ID_guest = input("Введите ID гостя: ")
                guest = get_guest(conn, ID_guest)
                print(guest)
            
            elif action_choice == '3':
                updated_guest_id = input("Введите ID книги для обновления: ")
                updated_guest = list(input("Введите обновленную информацию о госте через запятую\n(menu_menu_id, napitki_napitki_id, zakyski_zakyski_id, ФИО, Номер_столика): ").split(','))
                updated_guest.append(updated_guest_id)
                updated_guest_tuple = tuple(updated_guest)
                update_guest(conn, updated_guest_tuple)
            
            elif action_choice == '4':
                ID_guest_del = input("Введите ID гостя: ")
                delete_guest(conn, ID_guest_del)

        elif table_choice == '4':
            FIO = input("Введите ФИО: ")
            search_bar_guest_FIO(conn, FIO)
            continue

        elif table_choice == '5':
            avtor = input("Введите номер столика: ")
            search_bar_guest_stolik(conn, avtor)
            continue

        elif table_choice == '6':
            year = input("Введите guest_id: ")
            search_bar_guest_guest_id(conn, year)
            continue

        elif table_choice == '7':
            cost1 = input("Введите menu_id: ")
            search_bar_guest_menu_id(conn, cost1)
            continue
        else:
            print("Неверный пункт. Пожалуйста, попробуйте еще раз.")

    close_connection(conn)

if __name__ == "__main__":
    main()