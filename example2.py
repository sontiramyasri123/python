def main():
    name="ramya"
    city="vijayawada"
    age="20"
    string=("{0} is {1} old,stays at {2}")
    print(string.format(name,age,city))
    string=(" i am from {2},my name is {0} ,{1} years old")
    print(string.format(name,age,city))
if __name__=="__main__":
    main()
