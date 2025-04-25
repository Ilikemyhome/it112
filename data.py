from HW5 import app, tables, Dream_Cars

with app.app_context():
    tables.create_all()



    dreamCar_1 = Dream_Cars(make="Chevrolet", model="Corvette c8", year=2020, color="Baby Blue")
    dreamCar_2 = Dream_Cars(make="Ford", model="Mustang", year=2014, color="Black")
    dreamCar_3 = Dream_Cars(make="Mazda", model="Miata", year=1990, color="Red")
    dreamCar_4 = Dream_Cars(make="Jeep", model="Gladiator", year=2025, color="White")

    tables.session.add(dreamCar_1)
    tables.session.add(dreamCar_2)
    tables.session.add(dreamCar_3)
    tables.session.add(dreamCar_4)

    tables.session.commit()

    cars = Dream_Cars.query.all()
    print(cars)