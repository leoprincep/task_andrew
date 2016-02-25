import yaml
from yaml import load
import boto
from boto import ec2


with open ("test.yaml", "a+") as stream:
    a = yaml.load(stream)

sgs = a.keys()
sg1 = sgs[1]
sg2 = sgs[0]
sg1_desc = a[sg1]['description']
sg2_desc = a[sg2]['description']
sg1_rule_port1 = a[sg1]['ingress_rules'].keys()[0]
sg1_rule_port1_protocol = a[sg1]['ingress_rules'][sg1_rule_port1]
sg1_rule_port2 = a[sg1]['ingress_rules'].keys()[1]
sg1_rule_port2_protocol = a[sg1]['ingress_rules'][sg1_rule_port2]
sg2_rule_port1 = a[sg2]['ingress_rules'].keys()[0]
sg2_rule_port1_protocol = a[sg2]['ingress_rules'][sg2_rule_port1]

conn = ec2.connect_to_region('eu-west-1',aws_access_key_id='AKIAJH5VXIAIAQBEITGQ',aws_secret_access_key='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')

result = 0
count1 = 0
count2 = 0

def check_sg1(sg1,result,count1):
   for i in sg:
       if i.name == sg1:
           result = 'True'
           count1 = i
   return (result,count1)

def check_sg2(sg2,result,count2):
    for i in sg:
        if i.name == sg2:
            result = 'True'
            count2 = i
    return (result,count2)



sg = conn.get_all_security_groups()

sg1_result, sg1_count = check_sg1(sg1,result,count1)
if sg1_result == 'True':
    print "security group %s exists, adding rules"%sg1
    group1 = sg1_count
else:
    print "security group %s doesn't exists, creating now"%sg1
    group1 = conn.create_security_group(sg1,sg1_desc)

sg2_result, sg2_count = check_sg2(sg2,result,count2)
if sg2_result == 'True':
    print "security group %s exists, adding rules"%sg2
    group2 = sg2_count
else:
    print "security group %s doesn't exists, creating now"%sg2
    group2 = conn.create_security_group(sg2,sg2_desc)

group1.authorize(sg1_rule_port1_protocol,sg1_rule_port1, sg1_rule_port1, '0.0.0.0/0')
group1.authorize(sg1_rule_port2_protocol, sg1_rule_port2,sg1_rule_port2, '0.0.0.0/0')

group2.authorize(sg2_rule_port1_protocol, sg2_rule_port1, sg2_rule_port1, '0.0.0.0/0')

