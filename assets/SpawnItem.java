/**
 * Spawns the given ItemStack as an EntityItem into the World at the given position
 */
public static void spawnAsEntity(World world, BlockPos pos, ItemStack stack) {
    double xInBlock = world.rand.nextFloat() * 0.5F + 0.25D;
    double yInBlock = world.rand.nextFloat() * 0.5F + 0.25D;
    double zInBlock = world.rand.nextFloat() * 0.5F + 0.25D;
    EntityItem entityitem = new EntityItem(world, pos.getX() + xInBlock, pos.getY() + yInBlock, pos.getZ() + zInBlock, stack);
    world.spawnEntity(entityitem);
}