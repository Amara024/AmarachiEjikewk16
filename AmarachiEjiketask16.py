
#You are the facilitator in the ada program for 3 tracks
#list of student
#['Amaka disappoint', 'Nedu Japan', 'Pretty Cynthia', 'Nedu Japan', 'Pretty Cynthia', 'Pretty Cynthia' ]
#('Jon Doe'. 'John doe', 'John doe', 'Jon Bellion', 'Jon Bellion', 'Jon doe')
#{'Ada Ada', 'Pyhon ezege', 'Dog catcher', 'Bitrus Beetroot', 'Doja cat' 'Beja rat'} 
#data track
#create a nested dictionary
#add score
#get the highest score for each track

student = {
    'data' : {'Amaka Disappoint':'67',
               'Nedu Japan' : '57',
               'Pretty Cynthia' : '75',
               'Nedu Japan' : '57',
               'Pretty Cynthia':'75',
               'Pretty Cynthia' : '75'
    },

    'cloud' : {'Jon Doe' : '74',
                'John Doe' : '84',
                'John Doe' : '84',
                'Jon Bellion' : '51',
                'Jon Bellion' : '51',
                'Jon Doe' : '74'
    },
    'frontEnd' : {'Ada Ada' : '83',
                  'Pyhon Ezege' : '68',
                  'Dog Catcher' : '79',
                  'Bitrus Beetroot' : '49',
                  'Doja Cat' : '50',
                  'Beja Rat' : '47'
    }
}
print(student)
print(student['data']['Pretty Cynthia'])
print(student['cloud']['John Doe'])
print(student['frontEnd']['Ada Ada'])