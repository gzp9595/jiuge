# create database

import MySQLdb
import MySQLdb.cursors
import ConfigParser

try:
    conf = ConfigParser.ConfigParser()
    conf.read("config.cfg")
    db = MySQLdb.connect(
        host=conf.get('db', 'db_host'),
        user=conf.get('db', 'db_name'),
        passwd=conf.get('db', 'db_password'),
        db=conf.get('db', 'db_database'),
        cursorclass=MySQLdb.cursors.DictCursor)

    cursor = db.cursor()

    cursor.execute("drop table if exists result_all")
    
    sql = """create table if not exists result_all(
            id int not null AUTO_INCREMENT,
            user_id VARCHAR(45) NULL,
            type_top VARCHAR(100) NULL,
            itime DATETIME NULL,
            content VARCHAR(1000) NULL,
            ip VARCHAR(30) NULL,
            star VARCHAR(5) NULL,
            PRIMARY KEY (`id`))DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    db.commit()

    # cursor.execute("drop table if exists result")
    
    # sql = """create table if not exists result(
    #         user_id VARCHAR(45) NULL,
    #         type_top VARCHAR(60) NULL,
    #         content VARCHAR(100) NULL,
    #         PRIMARY KEY (`user_id`))DEFAULT CHARSET=utf8"""
    # cursor.execute(sql)

    # db.commit()

    cursor.execute("drop table if exists result_id")
    
    sql = """create table if not exists result_id(
            user_id VARCHAR(45) NULL,
            celery_id VARCHAR(45) NULL,
            list_num VARCHAR(45) NULL,
            PRIMARY KEY (`user_id`))DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    db.commit()

    cursor.execute("drop table if exists list_JJ")
    
    sql = """create table if not exists list_JJ(
            id int not null AUTO_INCREMENT,
            user_id VARCHAR(45) NULL,
            status VARCHAR(20) NULL,
            PRIMARY KEY (`id`))DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    db.commit()

    cursor.execute("drop table if exists list_CT")
    
    sql = """create table if not exists list_CT(
            id int not null AUTO_INCREMENT,
            user_id VARCHAR(45) NULL,
            status VARCHAR(20) NULL,
            PRIMARY KEY (`id`))DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    db.commit()

    cursor.execute("drop table if exists list_JJJ")
    
    sql = """create table if not exists list_JJJ(
            id int not null AUTO_INCREMENT,
            user_id VARCHAR(45) NULL,
            status VARCHAR(20) NULL,
            PRIMARY KEY (`id`))DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    db.commit()

    # cursor.execute("drop table if exists poem_map")
    
    # sql = """create table if not exists poem_map(
    #         id int not null AUTO_INCREMENT,
    #         type VARCHAR(200) NULL,
    #         result VARCHAR(1000) NULL,
    #         PRIMARY KEY (`id`))DEFAULT CHARSET=utf8"""
    # cursor.execute(sql)

    db.commit()

except MySQLdb.Error, e:
    print"Mysql Error %d: %s" % (e.args[0], e.args[1])
finally:
    cursor.close()
    db.close()
