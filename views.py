from django.shortcuts import render
from _mysql import connection
from CherryTest.util import getTable,dictfetchall
from django.utils.html import format_html



def show(req):
#     query = 'select * from employee'
#     cursor = connection.cursor()
#     # will return Cursor object
#     cursor.execute(query)
#     datalist = dictfetchall(cursor)
    user_details = []
#     for x in datalist:
#         user_details.append({'name':x['name'], 'email':x['email'], 'contact':x['contact'], 'action':"<a href='./edit?id=" + str(x['id']) + " '><i class='far fa-edit'></i></a> | " + 
#                             "<a href='./delete?id=" + str(x['id']) + " '><i class='fas fa-trash-alt'></i></a>"
#                              })
    table_data = getTable([
                            {'id':'mytable'},
                            {'header':[
                                        'SC_CODE',
                                        'SC_NAME',
                                        'SC_GROUP',
                                        'SC_TYPE',
                                        'OPEN',
                                        'HIGH',
                                        'LOW',
                                        'CLOSE',
                                        'LAST',
                                        'PREVCLOSE',
                                        'NO_TRADES',
                                        'NO_OF_SHRS',
                                        'NET_TURN'
                                      ]
                            },
                            {'content':user_details},
         
                        ])
    return render(req, 'index.html', {'emp_data':format_html(table_data)})

def search(req):
    name_search=req.POST.get('form_search')
    if name_search != '' and name_search != None:
        data=[name_search]
        try:
            query='select * from stock where name like %s'
            cursor=connection.cursor()
            cursor.excecute(query,data)
            searchlist = dictfetchall(cursor)
            search_details=[]
            for obj in searchlist:
                search_details.append(obj)
            table_data = getTable([
                            {'id':'stock_table'},
                            {'header':[
                                        'SC_CODE',
                                        'SC_NAME',
                                        'SC_GROUP',
                                        'SC_TYPE',
                                        'OPEN',
                                        'HIGH',
                                        'LOW',
                                        'CLOSE',
                                        'LAST',
                                        'PREVCLOSE',
                                        'NO_TRADES',
                                        'NO_OF_SHRS',
                                        'NET_TURN'
                                      ]
                            },
                            {'content':search_details},
         
                        ])
            return render(req, 'index.html', {'emp_data':format_html(table_data)})    
        except Exception as e:
            print(e.message)
        finally:
            connection.close()
            cursor.close()
    else:
        return render(req,'index.html',{})                
            
            