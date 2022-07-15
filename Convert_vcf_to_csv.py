#####################################################
#   Script for: Converting *.vcf data to *.txt file #       
#   Output: written to txt file                     #
#   Input files: All.vcf                            #
#####################################################

import os
import sys
import csv

# Make sure the program runs in current directory
path = os.getcwd()
os. chdir(path)

# Pharse data in VCF file.
def pharseVCFdata():
    
    temp_list = []      # temp list to store block for processing
    append_flag = 0
    tel_flag = 0     # Keeps track of the each block 
                                    # Check for multiple appearance of Phone no:
    name = " "           # Variable for name  
    phoneNum1 = " " 
    phoneNum2 = " " 
    phoneNum3 = " "
    header = ['name', 'Phone_1', 'Phone_2', 'Phone_3']
    
    VCFdata = open('All.vcf','r')
    lines = VCFdata.readlines()
    
    csvFile = open('Contacts.csv', 'w')
    writer = csv.writer(csvFile)
    writer.writerow(header)
        
    for line in lines:
        # Check each block between BEGIN and END
        # Check for line starting with word "BEGIN:"
        if "BEGIN:" in line:
            append_flag = 1        
        if "END:" in line and append_flag == 1:
        # check for Name and Phone no inside stored list.
       
            for item in temp_list:           
                if "FN:" in item:
                    name = item.strip().split(":")
                    name = name[1]
                    #name = item[3:]
                if "TEL;" in item:

                    if tel_flag ==0:
                        phoneNum1 = item.strip().split(":")
                        phoneNum1 = phoneNum1[1]
                        phoneNum1 = str(phoneNum1)
                    if tel_flag == 1:
                        phoneNum2 = item.strip().split(":")
                        phoneNum2 = phoneNum2[1]
                        phoneNum2 = str(phoneNum2)
                    if tel_flag == 2:
                        phoneNum3 = item.strip().split(":")
                        phoneNum3 = phoneNum3[1]
                        phoneNum3 = str(phoneNum3)
                    tel_flag = tel_flag+1
            print(name+phoneNum1+phoneNum2+phoneNum3)
            data = [name,phoneNum1,phoneNum2,phoneNum3]
            writer.writerow(data)
			
            #clear all the variable for processing next block
            append_flag = 0
            tel_flag = 0
            name = " "       
            phoneNum1 = " " 
            phoneNum2 = " "
            phoneNum3 = " "
            temp_list.clear()
			
    # store(append) each block in a temp_list
        if append_flag == 1:
            temp_list.append(line)
    # temp_list cleared after collecting data
        if append_flag == 0:        
            temp_list.clear()
        
    VCFdata.close()
    csvFile.close()

pharseVCFdata() 


__CreatedBy__ = 'Krishmar'
__CreatedOn__ = '14/07/22'
