import datetime
from sqlalchemy import Date, DateTime, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from ..utils.db import Base

# Modelos para Administrar Lecturas de Generación  

class Facility(Base):
    __tablename__ = "facilities"

    facility_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    facility_name = Column(String(100), nullable=False, unique=True, index=True)
    facility_address = Column(String(100))
    facility_phone = Column(String(10))
    facility_active = Column(Boolean(), default=True)

    created_on = Column(DateTime(), default=datetime.datetime.now)
    updated_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self) -> str:
        return  "Cookie(facility_name='{self.facility_name}', facility_address='{self.facility_address}', facility_phone='{self.facility_phone}')".format(self=self)
    
    def __str__(self):
        return self.facility_name
        

class GenType(Base):
    __tablename__ = "gen_types"

    gen_type_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    gen_type_name = Column(String(100), nullable=False, unique=True, index=True)
    gen_type_active = Column(Boolean(), default=True)

    created_on = Column(DateTime(), default=datetime.datetime.now)
    updated_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self) -> str:
        return  "GenType(gen_types_name='{self.facility_name}')".format(self=self)

    def __str__(self):
        return self.gen_type_name


class Machine(Base):
    __tablename__ = "machines"

    machine_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    facility_id = Column(Integer(), ForeignKey("facilities.facility_id"))
    gen_type_id = Column(Integer(), ForeignKey("gen_types.gen_type_id"))
    machine_name = Column(String(100), nullable=False, unique=True, index=True)
    machine_active = Column(Boolean(), default=True)

    created_on = Column(DateTime(), default=datetime.datetime.now)
    updated_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    # Relaciones
    facility = relationship("Facility", backref=backref("machines", order_by=machine_name))#Relacion M:1
    gen_type = relationship("GenType", backref=backref("machines", order_by=machine_name))#Relacion M:1

    def __repr__(self) -> str:
        return  "Machine(machine_name='{self.machine_name}')".format(self=self)
    
    def __str__(self):
        return self.machine_name


class Reading(Base):
    __tablename__ = "readings"

    reading_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    machine_id = Column(Integer(), ForeignKey("machines.machine_id"))
    reading_date = Column(Date(), nullable=False)
    reading_hour = Column(String(5), nullable=False)
    reading_value = Column(Integer, default=0)
    
    created_on = Column(DateTime(), default=datetime.datetime.now, nullable=False)
    updated_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

    # Relaciones
    machine = relationship("Machine", backref=backref("readings", order_by=reading_id))#Relacion M:1

# Modelos para Administrar Lecturas de Embalses

class Dam(Base):  
    __tablename__ = "dams"  # Tabla embalses

    dam_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    dam_name = Column(String(100), nullable=False, index=True)
    dam_level_max = Column(Integer(), nullable=False)
    dam_level_min = Column(Integer(), nullable=False)

    create_on = Column(DateTime(), default=datetime.datetime.now, nullable=False)
    update_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

class DamReading(Base):
    __tablename__ = "dam_readings"  # Tabla lectura de embalses

    dam_reading_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    dam_id = Column(Integer(), ForeignKey("dams.dam_id"))
    dam_reading_date = Column(Date(), nullable=False)
    dam_reading_value = Column(Integer, default=0)

    # Relaciones
    dam = relationship("Dam", backref=backref("dam_readings", order_by=dam_reading_id))

#  Modelos para Administrar Lecturas de Lineas

class ElectricLine(Base):  
    __tablename__ = "electric_lines"  # Tabla lineas electricas

    ele_line_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    ele_line_name = Column(String(100), nullable=False, index=True)
    ele_line_state = Column(String(100), nullable=False)
    
    create_on = Column(DateTime(), default=datetime.datetime.now, nullable=False)
    update_on = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)

class ElectricLineReading(Base):
    __tablename__ = "electric_line_readings"  # Tabla lectura de Lineas

    line_reading_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True, nullable=False)
    ele_line_id = Column(Integer(), ForeignKey("electric_lines.ele_line_id"))
    ele_line_reading_date = Column(Date(), nullable=False)
    ele_line_reading_hour = Column(String(5), nullable=False)
    ele_line_reading_value = Column(Integer(), default=0)
    
    # Relaciones
    ele_line = relationship("ElectricLine", backref=backref("electric_line_readings", order_by=line_reading_id))