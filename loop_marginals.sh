for s in 1 2 3 4 
do 
    echo Seed $s
    python experiments/gcsl_example_n11.py -S $s -E pointmass_rooms -K 2 &
done
wait
#for s in 5 6 7 8
#do 
#    echo Seed $s
#    python experiments/gcsl_example_n11.py -S $s -E pointmass_rooms -K 1 &
#done
#wait




#for s in 1 2 3 4 5 6 7 8
#do 
#    for e in pointmass_rooms
#    do
#	echo Environment $e Seed $s
        #python experiments/gcsl_example.py -S $s -E $e -K 1 &
#	python experiments/gcsl_example_n11.py -S $s -E $e -K 0 &
#    done
#  wait
#done
#wait

#for s in 0 1 2
#do 
#    for e in pusher door lunar pointmass_rooms pointmass_empty
#    do
#	echo Environment $e Seed $s
#        #python experiments/gcsl_example.py -S $s -E $e &
#	python experiments/gcsl_example_n11.py -S $s -E $e -K 0 &
#    done
#  wait
#done
#wait


#for s in 2
#do 
#    for e in pointmass_empty
#    do
#	echo Environment $e Seed $s
#        python experiments/gcsl_example.py -S $s -E $e -K 2 &
#	python experiments/gcsl_example_n11.py -S $s -E $e -K 2 &
#    done
#   wait
#done
#wait

#for s in 5 6 7 
#do 
#    for e in lunar
#    do
#	echo Environment $e Seed $s
#        python experiments/gcsl_example.py -S $s -E $e -K 3 &
#	python experiments/gcsl_example_n11.py -S $s -E $e -K 3 &
#    done
#   wait
#done
#wait



#
#for s in 1
#do 
#    for e in pointmass_empty pointmass_rooms lunar pusher door 
#    do
#	echo Environment $e Seed $s
#        python experiments/gcsl_example_n.py -S $s -E $e &
#    done
#done
#
#for s in 2
#do 
#    for e in pointmass_empty pointmass_rooms lunar pusher door 
#    do
#	echo Environment $e Seed $s
#        python experiments/gcsl_example_n.py -S $s -E $e &
#    done
#done

#for k in 0 1 2 3 4 5
#do
#	python experiments/gcsl_example.py -K $k &
#	
#done
#wait

#for k in 0 1 2 3 4 5
#do
#	python experiments/gcsl_example_n11.py -K $k &
#	
#done
#wait


#for k in 2 3 
#do
#	python experiments/gcsl_example_n11.py -K $k &
#	python experiments/gcsl_example.py -K $k &
#done
#wait




exit 0
