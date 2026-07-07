def CheckVowel(Ch):
    if Ch == 'a' or Ch == 'e' or  Ch == 'i' or Ch =='o' or Ch == 'u':
        print("Character is Vowel")
    else:
        print("Character is Consonant")


def main():
    Value = input("Enter the Character")
    CheckVowel(Value)






if __name__ =="__main__":
    main()