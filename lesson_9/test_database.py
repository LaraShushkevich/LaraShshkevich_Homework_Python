from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert len(names) == 5


def test_insert_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    initial_count = connection.execute(text(
                             "select count (*) from subject")).scalar()

    sql = text("insert into subject (subject_id, subject_title)"
               " values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 555, 'new_title': 'new'})

    final_count = connection.execute(text(
                              "select count (*) from subject")).scalar()

    sql = text("delete from subject where subject_id = :new_id")
    connection.execute(sql, {"new_id": 555})

    assert final_count - initial_count == 1

    transaction.commit()
    connection.close()


def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("insert into subject (subject_id, subject_title)"
               " values (:new_id, :new_title)")
    connection.execute(sql, {"new_id": 111, "new_title": 'to update'})

    sql = text("update subject set subject_title = :subject_title "
               "where subject_id = :subject_id")
    connection.execute(sql, {"subject_title": 'new title', "subject_id": 111})

    sql = text("select * from subject where subject_id = :subject_id")
    res = connection.execute(sql, {'subject_id': 111})
    row = res.mappings().all()
    assert len(row) == 1
    assert row[-1]["subject_title"] == 'new title'

    sql = text("delete from subject where subject_id = :new_id")
    connection.execute(sql, {"new_id": 111})

    transaction.commit()
    connection.close()


def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()

    initial_count = connection.execute(text(
                             "select count (*) from subject")).scalar()

    sql = text("insert into subject (subject_id, subject_title)"
               " values (:new_id, :new_title)")
    connection.execute(sql, {"new_id": 777, "new_title": 'to delete'})

    sql = text("delete from subject where subject_id = :subject_id")
    connection.execute(sql, {"subject_id": 777})

    final_count = connection.execute(text(
                              "select count (*) from subject")).scalar()

    assert initial_count == final_count

    transaction.commit()
    connection.close()
