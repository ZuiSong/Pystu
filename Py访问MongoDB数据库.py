import pymongo


def main():
    conn = pymongo.MongoClient(host='localhost', port=27017)
    db = conn["spider"]
    c = db['bus'].find({'cityname': '长沙'})

    resdata = {}
    retresdata = {}
    stanames = []
    for d in c:
        rotename = d['rotename']
        data = d['data']
        retdata = d['returnData']
        for staorder in data:
            staname = data[staorder]

            if staname not in stanames:
                stanames.append(staname)

            if staname in resdata:
                resdata[staname].append(rotename)
            else:
                resdata[staname] = [rotename]

        for staorder in retdata:
            staname = retdata[staorder]

            if staname not in stanames:
                stanames.append(staname)

            if staname in retresdata:
                retresdata[staname].append(rotename)
            else:
                retresdata[staname] = [rotename]

    for sta in stanames:
        busrotes = resdata[sta] if sta in resdata else " "
        retbusrotes = retresdata[sta] if sta in retresdata else " "

        ressta = {'staname': sta,
                  'busrotes': busrotes,
                  'retbusrotes': retbusrotes
                  }
        db.station.insert(ressta)


if __name__ == '__main__':
    main()
