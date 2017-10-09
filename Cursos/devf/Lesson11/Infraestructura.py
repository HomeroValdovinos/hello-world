# Encoding
# -*- coding: utf-8 -*-


class Infraestructura(object):

    def __init__(self, database, application, connection, ticket, users, port):
        self.database = database
        self.application = application
        self.connection = connection
        self.ticket = ticket
        self.users = users
        self.port = port

    def checkstatus(self):
        if self.connection == "Open" or self.connection == "Open":
            return True
        else:
            return False

    def checkports(self):
        if self.port == "8080":
            print("This port can't be used")
        else:
            print("The port is available")

    def countusers(self):
        if self.users > 100:
            print("The server has limited of users and it has:", self.users)
            return self.users
        elif self.users < 1:
            print "The server doesn't have users"
            return self.users


class Monitor(Infraestructura):
     def __init__(self, database, application, connection, ticket, users, port, rack_loc, type_net, usage):
         super(Infraestructura, self).__init__(database, application, connection, ticket, users, port)
         self.rack_loc = rack_loc
         self.type_net = type_net
         self.usage = usage

    def get_location(self):
         print("The rack is located in :", self.rack_loc)


zappdb = Monitor("Sybase", "Perl", "open", "REQ929929", 121, "1000", "Zapopan", "SAN", "56%")
print(zappdb.get_location())



#
# server1 = Infraestructura("Oracle", "Java", "Open", "123", 2, "8001")
# print(server1.checkstatus())
# print("The application is: ", server1.application)
# server1.checkports()
# server1.countusers()
#
# server2 = Infraestructura("SQL Server", "C#", "Down", "REQ123455", 101, "8002")
# print(server2.checkstatus())
# print("The application is: ", server2.application)
# server2.checkports()
# server2.countusers()
#
# server3 = Infraestructura("DB2", "Python", "open", "REQ743743", 3, "8080")
# print(server2.checkstatus())
# print("The application is: ", server3.application)
# server3.checkports()
# server3.countusers()


