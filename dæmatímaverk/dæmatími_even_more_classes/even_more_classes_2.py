# The Sales class goes here
class Sales:
    def __init__(self, data):
        self.__data = [float(sale) for sale in data.split()]
    
    def get_average(self):
        return sum(self.__data) / len(self.__data)

    def add_sale(self, new_sale):
        self.__data.append(new_sale)


# The main program starts here
def read_data_from_file(file_name):
    file_stream = open(file_name, 'r')
    data = file_stream.read()
    file_stream.close()
    return data


def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()