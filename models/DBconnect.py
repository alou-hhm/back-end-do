import pymysql
import datetime

class DBconnect:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='159.75.72.254',port=3306, user='root', passwd="HHM135#", db='HHM'
                )
            self.cur = self.conn.cursor()
        except e:
            print(e)

    # 测试查询代码 - 完成
    # 封装查询代码 - 完成
    # dbTable需要查询的表名称
    def dbQuery(self,dbTable):
        cur = self.cur
        sql = "SELECT * FROM "+dbTable
        cur.execute(sql)
        returnList = []
        for r in cur:
            returnList.append(r)
            #print(r)
        return returnList
         
    
    # 用户登陆判断查询
    def dbQuery_userLogin(self,user_id,user_pwd):
        conn = self.conn
        cur = self.cur
        dbTable = "user_info"
        sql  = "SELECT * FROM "+dbTable+" WHERE userId='"+user_id+"' and userPwd='"+user_pwd+"'"
        print(sql)
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print("操作异常：%s"%str(e))
            #错误回滚
            conn.rollback()
            return e
        # 返回第一个合适的信息 - 也只有一个合适的信息
        for r in cur:
            return r

    # 用户是否存在查询
    def dbQuery_user_is_already(self,user_id):
        conn = self.conn
        cur = self.cur
        dbTable = "user_info"
        sql  = "SELECT * FROM "+dbTable+" WHERE userId='"+user_id+"'"
        print(sql)
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print("操作异常：%s"%str(e))
            #错误回滚
            conn.rollback()
            return e
        # 返回第一个合适的信息 - 也只有一个合适的信息
        for r in cur:
            return r


    # 测试删除代码 - 完成
    # 封装删除代码 - 完成
    # dbTable 表名称 - needId 删除索引 - inputId 输入的值
    def dbDelete(self,dbTable,needId,inputId):
        conn = self.conn
        cur = self.cur
        sql = "DELETE from "+dbTable+" where "+needId+"="+inputId
        #sql = 'DELETE from user_info where userId='+inputId
        print(sql)
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print("操作异常：%s"%str(e))
            #错误回滚
            conn.rollback()
    
    # 测试插入代码 - 完成
    # 封装 - 特殊情况特殊判断 - 时间参数待处理
    # dbTable 表名称 - 插入参数
    def dbInsert(self,dbTable,*args):
        conn = self.conn
        cur = self.cur

        # python没有switch，本身switch需要哈希比较的，这和Python倡导的灵活性相互驳斥，反而会退化到IF-ELIF-ELSE级别
        # 所以就用if-elif-else进行特判表对应的sql语句
        sql = ""
        print(args)
        if dbTable == "user_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s,%s,%s,%s);"
        elif dbTable == "titlenumber_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s);"
        elif dbTable == "titlenote_info":
            # 这个表格第四个是时间参数，待处理 - 特判解决
            #datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            #print(args)
            #sql = "INSERT INTO "+dbTable+" VALUES('{0}','{1}','{2}',str_to_date('{3}','%%Y-%%m-%%d %%H:%%i:%%s'),'{4}');".format(*args)
            sql = "INSERT INTO "+dbTable+" VALUES('{0}','{1}','{2}','{3}','{4}');".format(*args)
        elif dbTable == "title_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
        elif dbTable == "subject_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s,%s);"
        elif dbTable == "load_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s);"
        elif dbTable == "load_info":
            sql = "INSERT INTO "+dbTable+" VALUES(%s,%s,%s);"

        print(sql)
        try:
            if dbTable == "titlenote_info": 
                cur.execute(sql)
            else:
                cur.execute(sql,args)
            conn.commit()
        except Exception as e:
            print("操作异常：%s"%str(e))
            #错误回滚
            conn.rollback()
            return False
        return True

    # 测试更新、修改代码 - 完成
    # 封装更新，修改代码 - 完成
    # dbTable 表名称 -  needValue 需要修改的值名 - inputValue 需要修改的值 - needId 查询的ID名 - inputId 查询的ID具体内容
    def dbUpdate_signled(self,dbTable,needValue,inputValue,needId,inputId):
        conn = self.conn
        cur = self.cur
        sql = "update "+ dbTable+" set "+needValue+"=\'"+inputValue+"\' where " + needId + "=" + inputId
        #sql = "update user_info set userPwd='666666' where userId='1111'"
        print(sql)
        try:
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            print("操作异常：%s"%str(e))
            #错误回滚
            conn.rollback()

    # 批量更新，想了想就不做了 -  咕咕咕
    def dbUpdate_all(self,dbTable):
        pass

    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = DBconnect()

    chooseTable = "user_info"
    inputDataTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(inputDataTime)
    print(db.dbQuery(chooseTable))
    #db.dbQuery(chooseTable)