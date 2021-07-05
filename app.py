from flask import Flask,render_template,request
import sys
import hashlib
app=Flask(__name__)

def coprime(n):
            factorlist = []
            coprimelist = []
            for i in range(1,n):
                if n % i == 0:
                 factorlist.append(i)
                flag = True
            for k in range(len(factorlist)):
                if i % factorlist[k] == 0 and factorlist[k]!=1:
                 flag = False
                if flag == True:
                 coprimelist.append(i)
            return coprimelist

def extendedeuclidean(dividend,divisor):
        s=[1,0]
        t=[0,1]
        counter = 1 #starts off at index 1
        remainder = 2
        while(remainder != 0):
             quotient = dividend // divisor
             remainder = dividend % divisor
             dividend = divisor
             divisor = remainder
             svalue = s[counter-1] - quotient*s[counter]
             tvalue = t[counter-1] - quotient*t[counter]
             s.insert(counter+1,svalue)
             t.insert(counter+1,tvalue)
             counter = counter+1
             remainder = dividend % divisor
    
        return(s[-1],t[-1])

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        p = int(request.form['p'])
        q = int(request.form['q'])
        publickeyone = int(request.form['publickeyone'])
        originalmessage = int(request.form['originalmessage'])
        # Encoded_message=round((p/q),3)
        str=(request.form['str'])
        
        s=str
        x=str
        
        publickeytwo = p*q

        privatekeytwo = publickeytwo

        coprime_n = coprime(publickeytwo)

        coprime_n_size = (p-1)*(q-1)

        if len(coprime_n) == coprime_n_size:
         print("Successful check of co-prime")
        else:
         print("Went wrong somewhere")

        coprime_phi_n = coprime(coprime_n_size)

        combinedlist = []

        for i in range(len(coprime_n)):
            if coprime_n[i] in coprime_phi_n and coprime_n[i] > 1 and coprime_n[i] < coprime_n_size:
                combinedlist.append(coprime_n[i])

# publickeyone = (int)(input("Enter the value of e\n"))

# print("Public keys: {},{}".format(publickeyone,publickeytwo))


        test,privatekeyone = extendedeuclidean(coprime_n_size,publickeyone)
        if privatekeyone < 0:
            privatekeyone = privatekeyone + coprime_n_size
    
    
# print("Private keys: {},{}. Note this would be kept secret in an industrial application".format(privatekeyone,privatekeytwo))




#TESTING
    
# originalmessage = (int)(input("Enter the original message\n"))

# print("Original message:{}".format(originalmessage))


        Encoded_message = (originalmessage ** publickeyone) % publickeytwo

# print("Encoded message:{}".format(encoded))

        decoded = (Encoded_message**privatekeyone) % publickeytwo

# print("Decoded message:{}".format(decoded))
        # encode the string
        encoded_str = s.encode()
  
# create sha3-256 hash objects
        obj_sha3_256 = hashlib.sha3_256(encoded_str)
  
# print in hexadecimal
        # print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())

        encoded_st = s.encode()
  
# create sha3-384 hash objects
        obj_sha3_384 = hashlib.sha3_384(encoded_st)
  
# print in hexadecimal
        # print("\nSHA3-384 Hash: ", obj_sha3_384.hexdigest())

        encoded_stri=s.encode()
# create a sha3 hash object
        hash_sha3_512 = hashlib.new("sha3_512", s.encode())
  
        # print("\nSHA3-512 Hash: ", hash_sha3_512.hexdigest())


        return render_template('index.html',p=p,q=q,originalmessage=originalmessage,publickeyone=publickeyone,Encoded_message=Encoded_message,decoded_message=decoded,
        x=x,a=obj_sha3_256.hexdigest(),b=obj_sha3_384.hexdigest(),c=hash_sha3_512.hexdigest())
      
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)