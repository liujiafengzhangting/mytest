import pymysql

# python2用到mysql数据库驱动：MySQLdb
# python3用到mysql数据库驱动：pymysql

# 将python3的mysql驱动转换成python2的数据库驱动
# After this function is called, any application that imports MySQLdb or
#     _mysql will unwittingly actually use pymysql
pymysql.install_as_MySQLdb()