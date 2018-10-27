import time
import datetime
import re
import os
import sys
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'	


year = 2018
path = ""+str(datetime.datetime.now()).replace(" ", "-")
filename = path+"/"+str(datetime.datetime.now()).replace(" ", "-")+".html"
logg = str(datetime.datetime.now()).replace(" ", "-")+".log"

os.mkdir(path, 0755 )
files = ""
i =1

def htmlheader():
    html ="""
	<!doctype html>
	<html>
	<head>
	<title>Logs Forensic Investigator SSH/SFTP</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.1/css/bootstrap.css">
	<link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">
	<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
	<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
	<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
	<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.html5.min.js"></script>
	</head>
	<script type="text/javascript">
		$(document).ready(function() {
		    $('#example').DataTable( {
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
			"language": {
            			"url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        		},
			buttons: [
			    'copyHtml5',
			    'excelHtml5',
			    'csvHtml5',
			    'pdfHtml5'
			]
		    } );
		} );
	</script>
    """
    return html

def createTable(files):
	html = """
	<table id="example" class="table table-bordered display" style="width:100%" >
        <thead>
            <tr>
                <th>ID</th>
                <th>Month</th>
                <th>Day</th>
                <th>Hours</th>
                <th>Hostname</th>
                <th>App</th>
		<th>MSG</th>
            </tr>
        </thead>
        <tbody>
		""" +files+"""
	</tbody>
        <tfoot>
            <tr>
                <th>ID</th>
                <th>Month</th>
                <th>Day</th>
                <th>Hours</th>
                <th>Hostname</th>
                <th>App</th>
		<th>MSG</th>
            </tr>
        </tfoot>
    </table>

	"""
	return html

def htmlbody(tblog):
	html ="""
		<body>
			<div class="container-fluid">
                               	<div class="jumbotron">
                                          
					  	<table border ="0">
							<tr>
								<td>
									<h1 class="display-4">LOGFISSH</h1>
								 	<p class="lead">Logs Forensic Investigator SSH/SFTP</p>
								</td>
							</tr>
						</table>
					</div>
				 <div>""" + tblog+ """</div>
			</div>
		<br><br><br><br><br><br><br>
		</body>
		</html>
	"""
	return html

def CreateReport(filename,content):
	file = open(filename, "w")
	file.write(content)
	file.close()


def ParseDate(line):
	date = re.search(r'^[A-Za-z]{3}\s*[0-9]{1,2}\s[0-9]{1,2}:[0-9]{2}:[0-9]{2}', line)
	if date is not None:
		return date.group(0)


def banner():
    print """
			       |||      |||
			       | |  __  | |
		|-|_____-----/   |_|  |_|   \-----_____|-|
		|_|_________{   }|  (^) |{  }__________|_|
		 ||          |_| |   ^  | |_|          ||
		 |              \|  /\  |/              |
		 |               \ |--| /               |
		 =               \ |__| /               =
		 +               \      /               +
				  \    /
				  \    /
				   \  /
				   \  /
				   \  /
				   \  /  LOGFISHH 1.0 - Logs Forensic Investigator SSH/SFTP
				   \  /                            Developer :@svelizdonoso       
				   \  /             GitHub: https://github.com/SVelizDonoso
				    \/                              Mail:cyslabs@gmail.com        
                                                           
                                                     
    Use: python logfissh.py --file /var/log/auth.log
     	 python logfissh.py --file /var/log/auth.log --animation 
	 python logfissh.py --file /var/log/auth.log --webm 
    Options: 
	 python logfissh.py -h


    """

def help():
 
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--file', help='File Logs ')
	parser.add_argument('-a','--animation',action='store_true',help='Animation logs access')
	parser.add_argument('-v','--webm',action='store_true', help='output animation to .webm')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        return vars(parser.parse_args())

if __name__ == "__main__":
	banner()
	res = help()
	print ""
	print ""
	if res['file']:
		f= open(res['file'])
        	file_as_list = f.readlines()
		print bcolors.OKGREEN+ "\n[*] Analyzing Logs [*] "+bcolors.ENDC
		for line in file_as_list:
		    respon = line.split(" ",5)
		    if respon[1] == "":
			    respon = line.split(" ",6)
			    files +="""
				    <tr>
					<td>""" + str(i)+ """</td>
					<td>""" + respon[0]+ """</td>
					<td>""" + respon[2]+ """</td>
					<td>""" + respon[3]+ """</td>
					<td>""" + respon[4]+ """</td>
					<td>""" + respon[5]+ """</td>
					<td>""" + respon[6]+ """</td>
				    </tr>
		    """
		    else:
			    files +="""
				    <tr>
					<td>""" + str(i)+ """</td>
					<td>""" + respon[0]+ """</td>
					<td>""" + respon[1]+ """</td>
					<td>""" + respon[2]+ """</td>
					<td>""" + respon[3]+ """</td>
					<td>""" + respon[4]+ """</td>
					<td>""" + respon[5]+ """</td>
				    </tr>
		    """
		    if ("Failed" in line) or ("Accepted" in line):
			date_stamp_found = ParseDate(line)
			date_time_obj = datetime.datetime.strptime(str(year)+" "+date_stamp_found, '%Y %b %d %H:%M:%S')
			dt = time.mktime(date_time_obj.timetuple())
			if "invalid" in line:
			     line_list = line.split()
			     user = line_list[10]
			     ip = line_list[12]
			     event="M"
			     event_print="Failed"
			else:
			     line_list = line.split()
			     user = line_list[8]
			     ip = line_list[10]
			     event="M"
			     event_print="Failed"
			if "Accepted password for" in line:
			    line_list = line.split()
			    user = line_list[8]
			    ip = line_list[10]
			    event="A"
			    event_print="Accepted" 
			if "Accepted publickey for" in line:
			    line_list = line.split()
			    user = line_list[8]
			    ip = line_list[10]
			    event="A"
			    event_print="Accepted"
			with open(logg,"a+") as out:
				out.write('%s|%s|%s|/%s/%s/%s/%s.%s\r\n' % (int(dt),ip,event,event_print,user,ip,dt,user))
		    i = i +1

		print bcolors.OKGREEN+ "\n[*] Creating LOGS Report in HTML "+bcolors.ENDC
		head = htmlheader()
		tb = createTable(files)
		fin= htmlbody(tb)
		CreateReport(filename,head+fin)
		print bcolors.OKGREEN+ "\n[*] The Report Was created Route: "+filename+bcolors.ENDC
		print "\n\n"
		if res['animation']:
			os.system("gource "+logg+" --fullscreen --camera-mode track --log-format custom --key --max-files 0 --file-idle-time 0 ")
		if res['webm']:
			print bcolors.OKGREEN+ "\n[*] Creation  webm: [*] "+bcolors.ENDC
			print ""
			print "This operation may take several minutes...."
			print ""
			os.system("gource "+logg+" --camera-mode track -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libvpx -b 10000K gource.webm ")
			print bcolors.OKGREEN+ "\n[*] Finished Work  [*] "+bcolors.ENDC
			print " "
			print " "
			
	else:
		sys.exit()	
	





