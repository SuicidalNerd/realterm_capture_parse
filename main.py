with open('capture_demo.txt','r') as f:
    line_list=[]
    recnik = {}
    for line in f:
        strip_lines=line.strip()
        listli=str(strip_lines.split())
        m=line_list.append(listli)
        recnik=dict(listli.split(','))
        recnik.update()