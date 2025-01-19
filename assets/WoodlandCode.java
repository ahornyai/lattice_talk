// (chunkX,chunkZ) is being loaded, and this function checks if it should generate a Woodland Mansion
protected boolean canSpawnStructureAtCoords(int chunkX, int chunkZ) {

    // divide by 80, rounding down, to determine which "Woodland region" (my made up term) we're considering
    int woodlandRegionX = Math.floorDiv(chunkX, 80);
    int woodlandRegionZ = Math.floorDiv(chunkZ, 80);

    // seed the random number generator deterministically in a way that's unique to this Woodland region
    Random random = this.world.setRandomSeed(woodlandRegionX, woodlandRegionZ, 10387319);

    // pick which chunk within this region will get the Woodland Mansion
    int woodlandChunkX = woodlandRegionX * 80 + (random.nextInt(60) + random.nextInt(60)) / 2;
    int woodlandChunkZ = woodlandRegionZ * 80 + (random.nextInt(60) + random.nextInt(60)) / 2;

    // but is it *this* chunk, that we're loading right now?
    if (chunkX == woodlandChunkX && chunkZ == woodlandChunkZ) {
        // and, is this chunk in a biome that allows Woodland Mansions? (e.g. roofed forest)
        if (this.world.getBiomeProvider().areBiomesViable(chunkX * 16 + 8, chunkZ * 16 + 8, 32, ALLOWED_BIOMES)) {
            return true;
        }
    }

    return false;
}

// and here's what it calls in World.java:
public Random setRandomSeed(int seedX, int seedY, int seedZ) {
    // this.getWorldInfo().getSeed() is the overall seed of the entire map
    // which has been cracked long ago for 2b2t (it's -4172144997902289642)
    this.rand.setSeed(seedX * 341873128712L + seedY * 132897987541L + seedZ + this.getWorldInfo().getSeed());
    return this.rand;
}