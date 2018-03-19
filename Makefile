wae:
	python -W ignore experiment_wae.py

profiler:
	python -m cProfile -o profiling_results test.py
prepare:
	pip install -r requirements.txt

datasets: nodrift gradualslowfaster suddenrecuring sudden gradualreoccuring suddengradual blips suddenrecurringfaster

gui:
	java -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.gui.GUI

tiny:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s generators.RandomRBFGenerator -f datasets/tiny.arff -m 7000"

toyset:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s generators.RandomRBFGenerator -f datasets/toyset.arff -m 20000"

nodrift:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s generators.RandomRBFGenerator -f datasets/RBFNoDrift.arff -m 100000"
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (generators.LEDGenerator -n 20) -f datasets/LEDNoDrift.arff -m 100000"

gradualslowfaster:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (generators.HyperplaneGenerator -c 4 -k 5 -t 0.0010) -f datasets/HyperplaneSlow.arff -m 100000"
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (generators.HyperplaneGenerator -c 4 -k 5 -t 0.10) -f datasets/HyperplaneFaster.arff -m 100000"

suddenrecuring:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.RandomTreeGenerator -c 4) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 2 -r 2 -c 4) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 3 -r 3 -c 4) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 7 -c 4) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 11 -r 2 -c 4) -d (generators.RandomTreeGenerator -i 5 -r 3 -c 4) -a 90.0 -p 200000 -w 1 -r 3) -a 90.0 -p 200000 -w 1 -r 311) -a 90.0 -p 200000 -w 1 -r 23) -a 90.0 -p 200000 -w 1 -r 2) -a 90.0 -p 200000 -w 1) -f datasets/RandomTreeRecurring.arff -m 100000"

sudden:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.SEAGenerator -f 1) -d (ConceptDriftStream -s (generators.SEAGenerator -f 2) -d (ConceptDriftStream -s (generators.SEAGenerator -f 3)   -d (generators.SEAGenerator -f 4) -w 50 -p 250000 ) -w 50 -p 250000 ) -w 50 -p 250000) -f datasets/SEASudden.arff -m 100000"
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.SEAGenerator -i 1 -f 1 -b)  -d (ConceptDriftStream -s (generators.SEAGenerator -i 2 -f 2 -b) -d (ConceptDriftStream -s (generators.SEAGenerator -i 3 -f 3 -b) -d (ConceptDriftStream -s (generators.SEAGenerator -i 4 -f 4 -b)  -d (ConceptDriftStream -s (generators.SEAGenerator -i 5 -f 1 -b) -d (ConceptDriftStream -s (generators.SEAGenerator -i 6 -f 2 -b) -d (ConceptDriftStream -s (generators.SEAGenerator -i 7 -f 3 -b)  -d (ConceptDriftStream -s (generators.SEAGenerator -i 8 -f 4 -b) -d (ConceptDriftStream -s (generators.SEAGenerator -i 9 -f 1 -b) -d  (generators.SEAGenerator -i 10) -w 50 -p 100000) -w 50 -p 100000 ) -w 50 -p 100000) -w 50 -p 100000 ) -w 50 -p 100000 ) -w 50 -p 100000) -w 50 -p 100000 ) -w 50 -p 100000 ) -w 50 -p 100000) -f datasets/SEASuddenFaster.arff -m 100000"

gradualreoccuring:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.RandomRBFGenerator -c 4 -a 20) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -r 5 -i 5 -c 4 -a 20 -n 25) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -c 4 -a 20) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -r 13 -c 4 -a 20 -n 13) -d (generators.RandomRBFGenerator -r 31 -c 4 -a 20) -a 45.0 -p 125000 -w 250000 -r 21) -a 45.0 -p 125000 -w 250000 -r 23) -a 45.0 -p 125000 -w 250000 -r 2) -a 45.0 -p 125000 -w 250000) -f datasets/RBFGradualRecurring.arff -m 100000"
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s generators.RandomRBFGenerator -f datasets/RBFNoDrift.arff -m 100000"

suddengradual:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.LEDGeneratorDrift -d 3) -d (generators.LEDGeneratorDrift -d 2 -i 4 -n 30) -a 90.0 -p 500000 -w 10) -f datasets/LED.arff -m 100000"

blips:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.RandomRBFGenerator -c 4 -a 20) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -r 5 -i 5 -c 4 -a 20 -n 25) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -c 4 -a 20) -d (ConceptDriftStream -s (generators.RandomRBFGenerator -r 13 -c 4 -a 20 -n 13) -d (generators.RandomRBFGenerator -c 4 -a 20) -a 80.0 -p 249900 -w 200 -r 21) -a 80.0 -p 249900 -w 200 -r 23) -a 80.0 -p 249900 -w 200 -r 2) -a 80.0 -p 249900 -w 200) -f datasets/RBFBlips.arff -m 100000"

suddenrecurringfaster:
	java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask "WriteStreamToARFFFile -s (ConceptDriftStream -s (generators.RandomTreeGenerator -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 2 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 3 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 7 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 11 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 5 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 115 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 18 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 25 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 61 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 71 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 31 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 17 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 64 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 66 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 21 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 88 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 55 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 99 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 74 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 57 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 1 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 6 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 3 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 86 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 49 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 69 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 96 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 81 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 41 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 17 -r 1 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 71 -r 2 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 7 -r 3 -c 6) -d (ConceptDriftStream -s (generators.RandomTreeGenerator -i 13 -r 1 -c 6) -d (generators.RandomTreeGenerator -i 29 -r 2 -c 6) -a 90.0 -p 3000 -w 1 -r 63) -a 90.0 -p 3000 -w 1 -r 63) -a 90.0 -p 3000 -w 1 -r 63) -a 90.0 -p 3000 -w 1 -r 63) -a 90.0 -p 3000 -w 1 -r 33) -a 90.0 -p 3000 -w 1 -r 23) -a 90.0 -p 3000 -w 1 -r 32) -a 90.0 -p 3000 -w 1 -r 4) -a 90.0 -p 3000 -w 1 -r 7) -a 90.0 -p 3000 -w 1 -r 37) -a 90.0 -p 3000 -w 1 -r 73) -a 90.0 -p 3000 -w 1 -r 36) -a 90.0 -p 3000 -w 1 -r 89) -a 90.0 -p 3000 -w 1 -r 99) -a 90.0 -p 3000 -w 1 -r 97) -a 90.0 -p 3000 -w 1 -r 73) -a 90.0 -p 3000 -w 1 -r 43) -a 90.0 -p 3000 -w 1 -r 34) -a 90.0 -p 3000 -w 1 -r 38) -a 90.0 -p 3000 -w 1 -r 32) -a 90.0 -p 3000 -w 1 -r 3) -a 90.0 -p 3000 -w 1 -r 33) -a 90.0 -p 3000 -w 1 -r 77) -a 90.0 -p 3000 -w 1 -r 69) -a 90.0 -p 3000 -w 1 -r 96) -a 90.0 -p 3000 -w 1 -r 29) -a 90.0 -p 3000 -w 1 -r 36) -a 90.0 -p 3000 -w 1 -r 77) -a 90.0 -p 3000 -w 1 -r 37) -a 90.0 -p 3000 -w 1 -r 3) -a 90.0 -p 3000 -w 1 -r 311) -a 90.0 -p 3000 -w 1 -r 23) -a 90.0 -p 3000 -w 1 -r 2) -a 90.0 -p 3000 -w 1) -f datasets/RandomTreeRecurringFaster.arff -m 100000"

.PHONY: gui datasets
