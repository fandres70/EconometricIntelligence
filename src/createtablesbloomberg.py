/*Owner & Copyrights: Vance King Saxbe. A.*/""" Copyright (c) <2014> Author Vance King Saxbe. A, and contributors Power Dominion Enterprise, Precieux Consulting and other contributors. Modelled, Architected and designed by Vance King Saxbe. A. with the geeks from GoldSax Consulting and GoldSax Technologies email @vsaxbe@yahoo.com. Development teams from Power Dominion Enterprise, Precieux Consulting. Project sponsored by GoldSax Foundation, GoldSax Group and executed by GoldSax Manager."""from src.bloombergquote import *
import sqlite3 as lite
import string
import time

print ("Market Place Starts.......")

def pullprocess(ass):
        sds = bloombergquote.getquote(ass)
        return sds
def createtables(arguments):
        f = pullprocess(arguments[0])
        print ("Counter One Started.........")
        if f != []:
                con = lite.connect(arguments[1]+".db")
                fuck = f
                stmt = "CREATE TABLE IF NOT EXISTS "+fuck[0]+"table(ONNN TEXT, ATTT TEXT, PRIC REAL)"
                cur = con.cursor()
                cur.execute(stmt)
            
                con.commit()
                time.sleep(2)
                con.close()

    
    
/*email to provide support at vancekingsaxbe@powerdominionenterprise.com, businessaffairs@powerdominionenterprise.com, For donations please write to fundraising@powerdominionenterprise.com*/