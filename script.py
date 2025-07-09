import yaml
from collections import defaultdict 
def fasta_to_yaml(fasta_file, binder_chain, yaml_file):
    data = {}
    current_id = None

    with open(fasta_file, 'r') as f_in:
        for line in f_in:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:]  # Remove ">"
                data[current_id] = ""
            elif current_id:
                data[current_id] += line

    data2 = defaultdict(list)
    for key, value in data.items():
        com_dic = defaultdict(list)
        com_dic[key.split('|')[1]] = {'id': key.split('|')[0], 'sequence': value}
        
        data2['sequences'].append(dict(com_dic))                
    data2['properties']= [{'affinity':{'binder':binder_chain}}] 
    with open(yaml_file, 'w') as f_out:
        yaml.dump(dict(data2), f_out, sort_keys=False)

fasta_to_yaml('Q9JFD6_dna.fasta', 'A', 'Q9JFD6_dna2.yaml')
