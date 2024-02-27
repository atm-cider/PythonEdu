# MySQLdbのインポート
import MySQLdb

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='89989234',
    db='Mysql_test',
# テーブル内部で日本語を扱うために追加
    charset='utf8'
)
cursor = connection.cursor()

def MakeQuery(table_name):
    print("MakeQueryきた")
    table_name = "name_age_list"
    query = f"SELECT * FROM {table_name};"
    return query


def main():
    # テーブルの初期化
    cursor.execute("DROP TABLE IF EXISTS name_age_list")

    # テーブルの作成
    cursor.execute("""CREATE TABLE name_age_list(
        id INT(11) AUTO_INCREMENT NOT NULL, 
        name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci, 
        age INT(3) NOT NULL,
        PRIMARY KEY (id)
        )""")

    # データの追加
    cursor.execute("""INSERT INTO name_age_list (name, age)
        VALUES ('タロー', '25'),
        ('ジロー', '23'),
        ('サブロー', '21')
        """)

    # query = MakeQuery()
    table_name = "name_age_list"
    # query = f"SELECT * FROM {table_name};"
    query = MakeQuery(table_name)
    print(query)
    # 一覧の表示
    cursor.execute(query)

    for row in cursor:
        print(row)


if __name__ == "__main__":
    main()

# 保存を実行
# connection.commit()

# 接続を閉じる
# connection.close()