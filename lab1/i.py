n = int(input())
for _ in range(n):
    mail_adress = input()
    end = len(mail_adress) - 10
    if '@gmail.com' in mail_adress:
        print(mail_adress[0: end]) 

