import sqlite3
import xlrd
import xlwt

def createDataBase(cn):
	ess=sqlite3.connect(cn)
	ess.execute('''CREATE TABLE IF NOT EXISTS ALL_ESS 
	(PLANT TEXT,
	ESS_NUMBER TEXT PRIMARY KEY,
	IMPROVEMENT_SUBJECT TEXT,
	PROPOSAL_DATE TEXT,
	PROPOSAL_DEPARTMENT TEXT,
	PROPOSER TEXT,
	PROPOSER_NUMBER TEXT,
	APPROVED TEXT,
	STATUS TEXT,
	ACCEPTED_DAYS INTEGER,
	ACCEPTANCE_TIME TEXT,
	OFFICER_ACCEPTANCE_TIME TEXT,
	EXECUTOR_NUMBER TEXT,
	EXECUTOR TEXT,
	ASSIGN_PIC_PLANT TEXT,
	COMPLETION_DATA TEXT,
	EXECUTOR_DEPARTMENT TEXT,
	ESTIMATED_MANPOWER TEXT,
	ESTIMATED_BENEFIT TEXT,
	ACTUAL_MANPOWER TEXT,
	ACTUAL_BENEFIT TEXT,
	ESTIMATED_STARTDAY TEXT,
	ESTIMATED_DUEDAY TEXT,
	WHETHER_PAYMENT TEXT,
	MODIFIED_TIME TEXT,
	SEND_MAIL_TO_APPROVER TEXT,
	COMPLETE_DATE TEXT,
	IMPROVE_APPROVER_NAME TEXT,
	SITE_ID TEXT,
	PADEPT_ID TEXT,
	VAR_ASSIGN_PICDEPT_ID TEXT,
	VAR_PADEPT_MANAGER_ID TEXT,
	MODIFIER TEXT,
	FLOW_STEP_START_DATE TEXT,
	YEAR TEXT,
	SIGN_STEP TEXT,
	FOUNDER TEXT,
	ITEM_TYPE TEXT,
	PATH TEXT,
	DATA TEXT);''')

	
def readExcel(filename,cn):
	ess=sqlite3.connect(cn)
	
	workbook = xlrd.open_workbook(filename)
	sheet_name = workbook.sheet_names()[0]
	sheet = workbook.sheet_by_name(sheet_name)


	for i in range(0,sheet.nrows):
		temp = []
		for j in range(0,sheet.ncols):
			try:
				temp.append(sheet.cell(i,j).value)
			except (AttributeError):
				temp.append(None)
		#print(temp[39])
		
		ess.execute('''INSERT INTO ALL_ESS 
		(PLANT,ESS_NUMBER,IMPROVEMENT_SUBJECT,PROPOSAL_DATE,PROPOSAL_DEPARTMENT,
		PROPOSER,PROPOSER_NUMBER,APPROVED,STATUS,ACCEPTED_DAYS,
		ACCEPTANCE_TIME,OFFICER_ACCEPTANCE_TIME,EXECUTOR_NUMBER,EXECUTOR,ASSIGN_PIC_PLANT,
		COMPLETION_DATA,EXECUTOR_DEPARTMENT,ESTIMATED_MANPOWER,ESTIMATED_BENEFIT,ACTUAL_MANPOWER,
		ACTUAL_BENEFIT,ESTIMATED_STARTDAY,ESTIMATED_DUEDAY,WHETHER_PAYMENT,MODIFIED_TIME,
		SEND_MAIL_TO_APPROVER,COMPLETE_DATE,IMPROVE_APPROVER_NAME,SITE_ID,PADEPT_ID,
		VAR_ASSIGN_PICDEPT_ID,VAR_PADEPT_MANAGER_ID,MODIFIER,FLOW_STEP_START_DATE,YEAR,
		SIGN_STEP,FOUNDER,ITEM_TYPE,PATH,DATA) 
		VALUES (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],
		temp[6],temp[7],temp[8],temp[9],temp[10],
		temp[11],temp[12],temp[13],temp[14],temp[15],
		temp[16],temp[17],temp[18],temp[19],temp[20],
		temp[21],temp[22],temp[23],temp[24],temp[25],
		temp[26],temp[27],temp[28],temp[29],temp[30],
		temp[31],temp[32],temp[33],temp[34],temp[35],
		temp[36],temp[37],temp[38],temp[39]);''')
	ess.commit()


if __name__=='__main__':
	filename="活頁簿1.xlsx"
	cn="ess.db"
	createDataBase(cn)
	readExcel(filename,cn)