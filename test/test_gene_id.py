from pyensembl import EnsemblRelease

from nose.tools import assert_raises

ensembl = EnsemblRelease(77)

def test_gene_ids_of_gene_name_hla_release77():
    hla_a_gene_ids = ensembl.gene_ids_of_gene_name("HLA-A")
    assert 'ENSG00000206503' in hla_a_gene_ids, hla_a_gene_ids

    hla_b_gene_ids = ensembl.gene_ids_of_gene_name("HLA-B")
    assert 'ENSG00000234745' in hla_b_gene_ids, hla_b_gene_ids

    hla_c_gene_ids = ensembl.gene_ids_of_gene_name("HLA-C")
    assert 'ENSG00000204525' in hla_c_gene_ids, hla_c_gene_ids


def test_gene_id_of_invalid_name():
    with assert_raises(Exception):
        ensembl.gene_ids_of_gene_name("A wonderous pony sees through your soul")




