params.sam = null
process analyze_sam {
    input:
    path sam
    output:
    stdout

    script:
    """
    uv run python /data/classes/csic_bioinf01/users/bcbinf_colladoj/proyecto-sam/main.py $sam
    """
}

workflow {
    analyze_sam(params.sam).view()
}
