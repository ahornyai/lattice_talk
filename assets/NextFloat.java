public float nextFloat() {
    this.seed = (this.seed * multiplier + addend) % modulus; // update the seed
    int randomInteger = (int) (this.seed >> 24); // take the top 24 bits of the seed
    return randomInteger / ((float) (1 << 24)); // divide it by 2^24 to get a number between 0 and 1
 }