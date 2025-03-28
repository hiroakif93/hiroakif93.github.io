import sys,os,glob,json
path='/Users/hiroakifujita/works/HOMEPAGE/_contents/publications'
output='/Users/hiroakifujita/works/HOMEPAGE/_data/publications'

class RISConverter():
    
    def __init__(self, path):    
        self.path = path
    
    # Reading RIS file and getting tags    
    def read_ris(self, file):
        
        _dict = {}

        with open(file) as f:
            for line in f:
                info = line.split('  - ')
    
                if len(info) > 1:
                    key, value = info[0], info[1]
                    if key in _dict:
                        _dict[key].append(value.strip())
                    else:
                        _dict[key] = [value.strip()]
        self.ris_dict = _dict
        
        return _dict

    def convert_author(self):
        
        ris=self.ris_dict['AU']
        au_conv, au_full_conv = [], []

        for au in ris:
            name = [i.rstrip(',') for i in au.split(' ')]

            if len(name) > 2:
                index = [i for i, item in enumerate(name) if item.endswith('.')]
                result = [item for item in name if not item.endswith('.')]
                name_full_converted = result[0]+' '+name[index[0]]+' '+result[1]
                name_converted = result[0]+' '+name[index[0]]+' '+result[1][0]+'.'
            else:
                result = [item for item in name if not item.endswith('.')]
                name_full_converted = result[0]+' '+' '+result[1]
                name_converted = result[0]+' '+result[1][0]+'.'
            
            if name_converted == 'Fujita H.':
                name_converted = f"<b>{name_converted}</b>"
            au_conv.append(name_converted)
            au_full_conv.append(name_full_converted)
        
        self.au_line = ', '.join(au_conv)
        self.au_full_line = ', '.join(au_full_conv)
        self.ris_dict['AU'] = self.au_line        
    
    def find_DOI(self):
        keys = self.ris_dict.keys()        
        
        if 'UR' in keys:
            w = self.ris_dict['UR'][0].split('/')    
            self.ris_dict['DO'] = ['/'.join(w[-2:])]

    
    def get_title(self):
        if 'TI' not in self.ris_dict or len(self.ris_dict['TI']) == 0:            
            self.ris_dict['TI'] = [self.ris_dict['T1'][0]]
        
        return self.ris_dict['TI']

    def extract_as_json(self, keys):
        
        self.get_title()
        result = {key: self.ris_dict.get(key) for key in keys}
        #json.dump(result, open(f'{output}/publications.json', 'w'))
        return result
                    
    def main(self):
        files = glob.glob(self.path+"/*")
        
        publications = {}                        
        cnt = 1
        for i in files:
            print(i)
            self.read_ris(i)
            self.convert_author()
            if 'DO' not in self.ris_dict.keys():            
                self.find_DOI()
                
            pub_order = self.ris_dict['PY'][0][0:4] + '_' + str(cnt)
            cnt += 1    

            publications[pub_order] = self.extract_as_json(['AU', 'PY', 'TI', 'JO', 'DO'])
            # info = self.ris_dict['AU'] + ' '  
            # info += f"({self.ris_dict['PY'][0][0:4]})" + ' '
            # info += "<b>" + self.get_title()[0]+ '. ' + "</b>"
            # info += "<i>" + self.ris_dict['JO'][0]+ '. </i>'
            # info += f"<a href='https://doi.org/{self.ris_dict['DO'][0]}'>{self.ris_dict['DO'][0]}</a>"+ '. '
            
            # publications[pub_order] = info
        
        publications_sorted = sorted(publications.items(), key=lambda x:x[0], reverse=True)
        
        return publications_sorted
        
if __name__ == '__main__':
    
    riscon = RISConverter(path+"/published").main()
    json.dump(riscon, open(f'{output}/publications.json', 'w'), indent=4, separators=(",", ": "), sort_keys=True)
    # pub_keys = riscon.keys()
    # riscon_sorted = sorted(riscon.items(), key=lambda x:x[0], reverse=True)
    import pprint
    pprint.pprint(object=riscon)
    # with open(f'{output}/pulications.html', mode='w') as f:        
    #     for line in riscon_sorted:
    #         line_no = f'<li>' + "".join(line[1:])                    
    #         f.write(line_no+'</li>\n')
                