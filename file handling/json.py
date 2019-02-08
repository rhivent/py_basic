import json
help(json)
# buat dictionary
a = {
    'name' : 'max',
    'age' : 22,
    'marks' : [90,50,70,80],
    'pass' : True,
    'oject' : {
        'color' : ('red','blue')
    }
}

# convert type data to json
print(json.dumps(a)) # dictionary
print(json.dumps(a,indent=3,separators=(', ',' = '))) # memperlihatkan indentasi tiap elemen utk tampilan json lebih baik
# separator param pertama mereplace , dngn ,
# separator param kedua mereplace : dngn =
# akan tetapi lebih prefer pakai default , dan : karena notasi json seperti ini

print(json.dumps(a,indent=3,sort_keys=True)) # mesorting key sesuai abjad a-z

print(json.dumps(['1','2'])) # list
print(json.dumps(('1','2'))) # tuple
print(json.dumps('halo dunia')) # string
print(json.dumps(100)) # int
print(json.dumps(10.21)) # float
print(json.dumps(True)) # boolean True
print(json.dumps(False)) # boolean False
print(json.dumps(None)) # boolean False

# menconvert data mjd json file
with open('demo.json','w') as fh:
    fh.write(json.dumps(a,indent=2))

# read json data
with open('demo.json','r') as fh:
    # print(fh.read()) # reading as string value
    string = fh.read()
    json_value = json.loads(string) # converting to json atau dictionary
    print(json_value['name']) # mendapatkan value dngn key name
