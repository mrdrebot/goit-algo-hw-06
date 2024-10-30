class IDException(Exception):
    pass


def add_id(id_list, employee_id):
        if not employee_id.startswith('01'):
              raise IDException
        
        id_list.append(employee_id)
        return id_list

id_list = ["0100", "0101", "0102"]
new_id = "0103"

try:
    print(add_id(id_list, new_id))
except IDException:
      print("Entered id doesn't start by '01'!")
