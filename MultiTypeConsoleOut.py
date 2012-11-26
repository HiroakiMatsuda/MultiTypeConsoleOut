#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 \file MultiTypeConsoleOut.py
 \brief This component it is possible to input a pseudo signal of any data type
 \date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import ConfigPaser for read inifile
import ConfigParser as Conf
import csv
import tkcontroller

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
multitypeconsoleout_spec = ["implementation_id", "MultiTypeConsoleOut", 
		 "type_name",         "MultiTypeConsoleOut", 
		 "description",       "This component it is possible to input a pseudo signal of any data type", 
		 "version",           "1.0.0", 
		 "vendor",            "Matsuda Hiroaki", 
		 "category",          "DATA", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

class MultiTypeConsoleOut(OpenRTM_aist.DataFlowComponentBase):
	
	"""
	\class MultiTypeConsoleOut
	\brief This component it is possible to input a pseudo signal of any data type
	
	"""
	def get_filename(self, func):
                self.flag = func()

        def get_filename(self, func):
                self.filename = func()

	def __init__(self, manager):
		"""
		\brief constructor
		\param manager Maneger Object
		"""
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
		
		# Read ini file	
		self.conf = Conf.SafeConfigParser()
                self.conf.read('ini\consoleout.ini')
		
		self.type = self.conf.get('DATA', 'type')

		self.flag = 'none'
		if self.type.find('Seq') > 0:
			self.flag = 'Seq'
		
		if self.type == 'TimedShort':
			self._d_data = RTC.TimedShort(RTC.Time(0,0),0)
		
		elif self.type == 'TimedShortSeq':
			self._d_data = RTC.TimedShortSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedUShort':
			self._d_data = RTC.TimedUShort(RTC.Time(0,0),0)
		
		elif self.type == 'TimedUShortSeq':
			self._d_data = RTC.TimedUShortSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedLong':
			self._d_data = RTC.TimedLong(RTC.Time(0,0),0)
		
		elif self.type == 'TimedLongSeq':
			self._d_data = RTC.TimedLongSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedULong':
			self._d_data = RTC.TimedULong(RTC.Time(0,0),0)
		
		elif self.type == 'TimedULongSeq':
			self._d_data = RTC.TimedULongSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedFloat':
			self._d_data = RTC.TimedFloat(RTC.Time(0,0),0)
		
		elif self.type == 'TimedFloatSeq':
			self._d_data = RTC.TimedFloatSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedDouble':
			self._d_data = RTC.TimedDouble(RTC.Time(0,0),0)
		
		elif self.type == 'TimedDoubleSeq':
			self._d_data = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedString':
			self._d_data = RTC.TimedString(RTC.Time(0,0),0)
		
		elif self.type == 'TimedStringSeq':
			self._d_data = RTC.TimedStringSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedWString':
			self._d_data = RTC.TimedWString(RTC.Time(0,0),0)
		
		elif self.type == 'TimedWStringSeq':
			self._d_data = RTC.TimedWStringSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedChar':
			self._d_data = RTC.TimedChar(RTC.Time(0,0),0)
		
		elif self.type == 'TimedCharSeq':
			self._d_data = RTC.TimedCharSeq(RTC.Time(0,0),[])
			
		elif self.type == 'TimedWChar':
			self._d_data = RTC.TimedWChar(RTC.Time(0,0),0)
		
		elif self.type == 'TimedWCharSeq':
			self._d_data = RTC.TimedWCharSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedOctet':
			self._d_data = RTC.TimedOctet(RTC.Time(0,0),0)
		
		elif self.type == 'TimedOctetSeq':
			self._d_data = RTC.TimedOctetSeq(RTC.Time(0,0),[])
		
		elif self.type == 'TimedBool':
			self._d_data = RTC.TimedBool(RTC.Time(0,0),0)
		
		elif self.type == 'TimedBoolSeq':
			self._d_data = RTC.TimedBoolSeq(RTC.Time(0,0),[])

		else:
			print('The specified type did not mutch.Please check multitypeconsolein.ini')
		
		self._dataIn = OpenRTM_aist.InPort("data", self._d_data)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		self._conf_datanum = [1]
		self.log_flag = 1
		
		# </rtc-template>
		 
	def onInitialize(self):
		"""
		
		The initialize action (on CREATED->ALIVE transition)
		formaer rtc_init_entry() 
		
		\return RTC::ReturnCode_t
		
		"""
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("data",self._dataIn)
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		print('OnInitialize')

		self.loop_flag = 0
		
		return RTC.RTC_OK
	
	def onFinalize(self, ec_id):
		"""
	
		The finalize action (on ALIVE->END transition)
		formaer rtc_exiting_entry()
	
		\return RTC::ReturnCode_t
	
		"""
		
		print('OnFinalize')
	
		return RTC.RTC_OK
	
	def onActivated(self, ec_id):
		"""
	
		The activated action (Active state entry action)
		former rtc_active_entry()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		print('OnActivated')
	
		return RTC.RTC_OK
	
	def onDeactivated(self, ec_id):
		"""
	
		The deactivated action (Active state exit action)
		former rtc_active_exit()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
		print('OnDeactivated')

		return RTC.RTC_OK
	
	def onExecute(self, ec_id):
		"""
	
		The execution action that is invoked periodically
		former rtc_active_do()
	
		\param ec_id target ExecutionContext Id
	
		\return RTC::ReturnCode_t
	
		"""
                if self._dataIn.isNew():
                        self._d_data = self._dataIn.read()
                        data = self._d_data.data
                        data.append(self._d_data.tm.sec)
                        data.append(self._d_data.tm.nsec)
                        
                        if self.flag == 1:
                                if self.loop_flag == 0:
                                        self.csvfilename = self.filename + '.csv'
                                        self.csvfile = open(self.csvfilename, 'w')
                                        print('Start logging: %s' %self.csvfilename)
                                        self.writer = csv.writer(self.csvfile, lineterminator = '\n')
                                        self.writer.writerow(data)
                                        self.loop_flag = 1

                                elif self.loop_flag == 1:
                                        self.writer.writerow(data)

                        print data

                if self.flag == 0:
                        self.loop_flag = 0
                        self.csvfile.close()
                        self.flag = 1
                        print('End logging: %s' %self.csvfilename)
                        
                                
		return RTC.RTC_OK

	def set_flag(self, flag):
                self.flag = flag

        def set_filename(self, filename):
                self.filename = filename
                 
#def MultiTypeConsoleOutInit(manager):
#    profile = OpenRTM_aist.Properties(defaults_str=multitypeconsoleout_spec)
#    manager.registerFactory(profile,
#                            MultiTypeConsoleOut,
#                            OpenRTM_aist.Delete)
#
#def MyModuleInit(manager):
#    MultiTypeConsoleOutInit(manager)
#
#    # Create a component
#    comp = manager.createComponent("MultiTypeConsoleOut")

def main():
        tk = tkcontroller.TkController()
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.activateManager()
	# Register component
	profile = OpenRTM_aist.Properties(defaults_str=multitypeconsoleout_spec)
	mgr.registerFactory(profile,
                            MultiTypeConsoleOut,
                            OpenRTM_aist.Delete)
	comp = mgr.createComponent("MultiTypeConsoleOut")
	tk.get_flag(comp.set_flag)
	tk.get_filename(comp.set_filename)
	#comp.get_filename(tk.set_filename)
	#comp.get_flag(tk.set_flag)
	mgr.runManager(True)
	tk.root.mainloop()

if __name__ == "__main__":
	main()

