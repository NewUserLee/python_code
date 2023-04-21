import database_module

def main():
     # call a function from the database_module
     result = database_module.select()
     return result

if __name__ == '__main__':
    output = main()
print(output)
# ----------------------------------------------------------------------------------------------------------
