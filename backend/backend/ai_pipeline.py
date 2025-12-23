from bytez import Bytez

# Put your real Bytez API key later
sdk = Bytez("YOUR_BYTEZ_API_KEY")

def analyze_chunk(chunk_path):
    """
    Runs VideoMAE on a single video chunk
    """
    model = sdk.model("z12586/videomae-sft")
    output, error = model.run(chunk_path)

    if error:
        raise Exception(error)

    return output


def collect_scores(chunks):
    """
    Collects and globally ranks scores from all chunks
    """
    all_segments = []

    for idx, chunk in enumerate(chunks):
        result = analyze_chunk(chunk)

        for seg in result.get("segments", []):
            all_segments.append({
                "score": seg.get("score", 0),
                # convert chunk-local time to global video time
                "start": seg.get("start", 0) + idx * 300
            })

    # sort globally (highest score first)
    return sorted(all_segments, key=lambda x: x["score"], reverse=True)
