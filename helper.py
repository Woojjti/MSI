import os

def generate_stream(dbname, length, window, streams, force = False):
    if not force and os.path.isfile("%s.arff" % dbname):
        print("Skipping %s creation" % dbname)
        pass
    else:
        n_streams = len(streams)
        step = length // n_streams
        # Collect base streams
        cmd = "("
        for i, stream in enumerate(streams):
            p_cmd = None
            if i < n_streams - 1:
                p_cmd = "ConceptDriftStream -w %i -p %i -s (%s) -d (" % (
                    window, step, stream
                )
            else:
                p_cmd = stream
            cmd += p_cmd
        cmd += ")" * n_streams
        # Write to ARFF
        cmd = "WriteStreamToARFFFile -s %s -f %s.arff -m %i" % (
            cmd, dbname, length)
        # Use MOA
        cmd = "java -Xmx4G -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.DoTask \"%s\"" % cmd
        os.system(cmd)
