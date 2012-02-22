#! /usr/bin/env python
"""Generate some "soft science" data-set samples for use in Software Carpentry class
"""
import os, sys, random, numpy, time
this_directory = os.path.dirname(__file__)
FIRST_NAMES = open( os.path.join(this_directory, 'color_names.txt' )).read().splitlines()
LAST_NAMES = open( os.path.join(this_directory, 'animal_names.txt' )).read().splitlines()
CHOICES = ['red','orange','yellow','green','blue','indigo','violet']
BAD_CHOICES = ['black','white','grey','red-orange']
UNIQUE_NAMES = set()

def _names():
    while True:
        lasts = LAST_NAMES[:]
        random.shuffle( lasts )
        firsts = FIRST_NAMES[:]
        random.shuffle( firsts )
        for first,last in zip( firsts, lasts ):
            yield '%s %s'%(first,last)
_name = iter(_names()).next

def name( ):
    """Create a new, unique name"""
    n = _name()
    while n in UNIQUE_NAMES:
        n = _name()
    UNIQUE_NAMES.add( n )
    return n

def sample_data( rows=20):
    """Produce perfect sample data, as in the original spec for the project..."""
    result = [
        ['Subject','Count','DMX Score','Coda Score','Vinny Score','Zim Score','Subject Choice']
    ]
    for count in range( rows ):
        t = random.randint( 0, 100 )
        row = [ 
            name(), 
            t, 
            round(numpy.sin(t),3), 
            round(numpy.cos(t),3),
            round(numpy.tan(t),2),
            (t%8)**2,
            CHOICES[t%len(CHOICES)] 
        ]
        result.append( row )
    return result

def write_trial( results, filename ):
    with open( filename, 'w' ) as fh:
        for row in results:
            fh.write( ','.join( [str(x) for x in row] ) + '\n' )

# mutators which introduce errors into the data-sets...
def null_values( results, errors=1 ):
    for error in range( errors ):
        row = random.choice( results[1:] )
        column = random.randint( 1, 5 )
        row[column] = ''

def duplicate_names( results, errors=1 ):
    """Introduce condition where two users share the same name (potentially in different files)"""
    for error in range( errors ):
        row = random.choice( results[1:] )
        name = random.choice( list(UNIQUE_NAMES) )
        row[0] = name 
        break 

def comments( results, errors=1 ):
    for error in range( errors ):
        comment = [ '# we need to get more beds' ]
        results.insert( random.randint( 1, len(results)-1 ), comment )

def reverse_names( results ):
    for row in results[1:]:
        if len(row) > 1: # not a comment
            first,last = row[0].split()
            row[0] = '"%s, %s"'%( last, first )

def main():
    write_trial( sample_data(), 'sample_data.csv' )
    bad_sample = sample_data()
    reverse_names(bad_sample)
    null_values(bad_sample)
    comments( bad_sample )
    write_trial( bad_sample, 'bad_sample_data.csv' )
    path = os.path.join( this_directory, 'real_data' )
    for i in range( 50 ):
        count = random.randint( 5, 100 )
        data = sample_data(count)
        null_values( data, count//30 )
        duplicate_names( data, count//50 )
        comments( data, count//50 )
        if random.random() > .9:
            print 'reversing', i
            reverse_names(data)
        write_trial( data, os.path.join( path, 'trail-%04i.csv'%( i, )))
    

if __name__ == '__main__':
    main()
