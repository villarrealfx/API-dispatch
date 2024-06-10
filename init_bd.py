# from app.V1.utils.db import session_local, Base, engine
from app.V1.model.reading_model import Facility, GenType, Machine
from app.V1.model.user_model import User
from app.V1.utils.db import session_local, Base, engine

def run():
    '''

    '''
    session_local.bulk_save_objects(
        [
            GenType(gen_type_name = "Hidroeléctrica", gen_type_active = True),
            GenType(gen_type_name = "Termoeléctrica", gen_type_active = True),
            GenType(gen_type_name = "Electrógeno", gen_type_active = True),

            Facility(facility_name = "Fabricio Ojeda", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "San Agatón", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Planta Paez", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Peña Larga", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Masparro", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Don Luis Zambrano", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Termobarrancas", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Planta Tachira", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Batalla de Santa Inés", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Planta Monay", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Electrógenos Barinas", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Electrógenos Trujillo", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Electrógenos Merida", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Electrógenos Táchira", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),
            Facility(facility_name = "Electrógenos Apure", facility_address = "Sin Datos", facility_phone = "Sin Info", facility_active = True),

            Machine(machine_name = "FO Unidad 2", facility_id = 1, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "FO Unidad 3", facility_id = 1, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "SA Unidad 1", facility_id = 2, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "SA Unidad 2", facility_id = 2, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PP Unidad 1", facility_id = 3, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PP Unidad 2", facility_id = 3, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PP Unidad 3", facility_id = 3, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PP Unidad 4", facility_id = 3, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PL Unidad 1", facility_id = 4, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "PL Unidad 2", facility_id = 4, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "MP Unidad 1", facility_id = 5, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "MP Unidad 2", facility_id = 5, gen_type_id = 1, machine_active = True),
            Machine(machine_name = "DZ Unidad 1", facility_id = 6, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "DZ Unidad 2", facility_id = 6, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "DZ Unidad 3", facility_id = 6, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "TB Unidad 1", facility_id = 7, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 3", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 5", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 6", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 7", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 8", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 9", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 10", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 13", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 14", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "PT Unidad 15", facility_id = 8, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 1", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 2", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 3", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 4", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 5", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "SI Unidad 6", facility_id = 9, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "MO Unidad 1", facility_id = 10, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "MO Unidad 2", facility_id = 10, gen_type_id = 2, machine_active = True),
            Machine(machine_name = "Electrógenos Barinas ", facility_id = 11, gen_type_id = 3, machine_active = True),
            Machine(machine_name = "Electrógenos Trujillo ", facility_id = 12, gen_type_id = 3, machine_active = True),
            Machine(machine_name = "Electrógenos Merida ", facility_id = 13, gen_type_id = 3, machine_active = True),
            Machine(machine_name = "Electrógenos Tachira ", facility_id = 14, gen_type_id = 3, machine_active = True),
            Machine(machine_name = "Electrógenos Apure ", facility_id = 15, gen_type_id = 3, machine_active = True),
            
        ]
    )
    session_local.commit()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)  #Borrar las tablas o limpiarlas
    Base.metadata.create_all(engine)
    run()