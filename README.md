# Overview
- chapter 1 - theory:
  - the definition of a lattice
  - problems on lattices (SVP, CVP, approximate versions)
  - LLL algorithm
  - LLL visualization
- chapter 2 - practice:
  - lattice attacks / common problems
    - solving underdetermined linear equations (IrisCTF2025 - knutsacque)
      - introduction to solving CVP
      - Babai CVP algorithm and visualization
      - Kannan's embedding
    - ecdsa biased nonce (HNP, polynonce, putty P-521 exploit)
    - knapsack (hashmaster-9000 from ddc-nationals-2024)
    - RSA with partial info (Coppersmith, ImaginaryCTF - affine padding)
    - breaking truncated LCG (randar exploit - Minecraft hacking)
- chapter 3 - Building encryptions relying on lattice problems:
  - Introduction to LWE
  - Introduction to FHE

# CTF Challenges
- https://github.com/IrisSec/IrisCTF-2025-Challenges/blob/main/knutsacque/README.md
- https://github.com/FuzzyLitchi/writeups/blob/main/ddc-nationals-2024/hashmaster-9000/hashmaster-9000.md
- ImaginaryCTF - affine padding

# Useful tools
- https://github.com/josephsurin/lattice-based-cryptanalysis
- https://github.com/maple3142/lll_cvp
- https://github.com/rkm0959/Inequality_Solving_with_CVP
- https://github.com/defund/coppersmith
- https://github.com/keeganryan/flatter
- https://github.com/google/paranoid_crypto

# References
- The content of the presentation is largely based on Robin Jadoul's talk: https://ur4ndom.dev/static/files/latticetraining/practical_lattice_reductions.pdf
- Original explanation and diagrams for RANDAR exploit: https://github.com/spawnmason/randar-explanation
- https://theblupper.github.io/blog/posts/lattices/
- https://kel.bz/post/lll/
- https://www.math.elte.hu/thesisupload/thesisfiles/2024bsc_alkmat3y-sl45k6.pdf
- https://people.csail.mit.edu/vinodv/COURSES/CSC2414-F11/L4.pdf
- https://escholarship.org/content/qt4zt7x45z/qt4zt7x45z.pdf?t=ml518a
- https://www.di.ens.fr/~pnguyen/SLIDES/SlidesLuminy2010.pdf
- https://magicfrank00.github.io/writeups/posts/lll-to-solve-linear-equations/
- https://www.youtube.com/watch?v=MhYaVtS6_y4
- https://github.com/josephsurin/lattice-based-cryptanalysis/blob/main/tutorial.pdf
- https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/cvp.pdf
- https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/pq-kem/
- https://www.vicarius.io/vsociety/posts/understanding-a-critical-vulnerability-in-putty-biased-ecdsa-nonce-generation-revealing-nist-p-521-private-keys-cve-2024-31497
- https://minerva.crocs.fi.muni.cz/
- https://static.aminer.org/pdf/PDF/000/570/324/the_two_faces_of_lattices_in_cryptology.pdf
- https://cr.yp.to/bib/2001/coppersmith.pdf
- https://hal.science/hal-03045663/document
- https://www.jeremykun.com/2024/05/04/fhe-overview/