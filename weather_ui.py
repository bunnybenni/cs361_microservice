import time

if __name__ == "__main__":

    while True:
        # request input

        print("Enter the number of days out you'd like to request data for, or type 'exit' to exit.")
        raw_input = input()

        if raw_input != "exit":
            f = open('days_out.txt', 'w', encoding="utf-8")
            f.write(raw_input)
            f.close()

        print("Enter the zipcode you'd like to retrieve weather data from, or type 'exit' to exit.")
        raw_input = input()

        if raw_input != "exit":
            f = open('zipcode.txt', 'w', encoding="utf-8")
            f.write(raw_input)
            f.close()

            # sleep for 5 seconds
            time.sleep(5)

            # print data retrieved from microservice
            f = open('weather_data.txt', 'r', encoding="utf-8")
            line = f.readline()
            print(line)
            f.close()

        elif raw_input == "exit":
            break
