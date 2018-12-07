# All utility functions will be created here


def getTable(tablelist=[]):
    tableresult = ''
    _id = 'id='
    if tablelist == None:
        return tableresult
    for data in tablelist:
        if data.get('id'):
                _id += data.get('id')
                continue
        elif data.get('header'):
            tableresult += '<table class="table" ' + _id + '><thead class="thead-dark"></tr>'
            for item in data['header']:
                tableresult += '<th>' + item + '</th>'
            tableresult += '</tr></thead>'          
        elif data.get('content'):
            tableresult += '<tbody>'
            for obj in data['content']:
                tableresult += '<tr>'
                for x in obj.values():
                    tableresult += '<td>' + str(x) + '</td>'
                tableresult += '</tr>'    
            tableresult += '</tbody></table>'
                                
    return tableresult    

def dictfetchall(cursor):
    d = cursor.description 
    return [dict(zip([col[0] for col in d], row)) for row in cursor.fetchall()]