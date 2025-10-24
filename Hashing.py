name = []
clients = []
name1 = []
clients1 = []
no = []

m = int(input("Enter Size of Table: "))

class Probing:
    def hash_1(self,x):
        return x%m

    def prime_no(self,x):
        while True:
            for i in range(2,int(x/2)+1):
                if(x%i!=0):
                    return x
                x = x - 1

    def hash_2(self,x):
        p = self.prime_no(m-1)
        return p-(m%p)

    def display(self,name,no):
        print("Key------->Name------->TelephoneNo")
        for i in range(m):
            print(i,"------->",name[i],"------->",no[i])

    def search(self,no,name):
        flag = 0
        searchTel = input("Enter Name of client to search: ")
        for i in range(m):
            if(searchTel == name[i]):
                print("Telephone No: ",no[i])
                flag = 1
                break
        if(flag==0):
            print("Data not found!")

    def linear_probing(self,n):
        print("-----------> LINEAR PROBING <-----------")
        for i in range(n):
            nav = input("Enter Name of Client: ")
            no = int(input("Enter Telephone No: "))
            key = self.hash_1(no)
            temp = key

            if(clients[key]==0):
                name[key] = nav
                clients[key]= no
            else:
                while(1):
                    if(clients[temp]!=0):
                        if(temp == 9):
                            temp = 0
                        else:
                            temp = temp+1
                    else:
                        name[temp] = nav
                        clients[temp] = no
                        break
        self.display(name,clients)
        return clients

    def double_probing(self,n):
        print ( "-----------> DOUBLE PROBING <-----------" )
        for i in range ( n ) :
            nav = input ( "Enter Name of Client: " )
            no = int ( input ( "Enter Telephone No: " ) )
            key = self.hash_1 (no)
            temp = key

            if (clients1 [ key ] == 0) :
                name1 [ key ] = nav
                clients1 [ key ] = no
            else :
                point = 0
                while (1) :
                    if (clients1[ temp ] != 0) :
                        key2 = self.hash_2(clients1[i])
                        point = point + 1
                        temp = (key + (point * key2)) % m
                    else :
                        name1[ temp ] = nav
                        clients1[ temp ] = no
                        break
        self.display ( name1 , clients1 )
        return clients1

def main():
    n = int(input("Enter Total no. of clients: "))

    for k in range(m):
        clients.append(0)
        clients1.append(0)
        name.append(0)
        name1.append(0)

    obj = Probing()
    no = obj.linear_probing(n)
    obj.search(no,name)
    no = obj.double_probing(n)
    obj.search(no,name)

main()




