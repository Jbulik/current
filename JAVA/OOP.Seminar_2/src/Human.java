public class Human extends Actor implements ActorBehaviour{

    public Human(String name) {
        super(name);
    }

    @Override
    public void setMakeOrder() {
        super.isMakeOrder = true;

    }

    @Override
    public boolean isMakeOrder() {
        return isMakeOrder;
    }

    @Override
    public boolean isTakeOrder() {
        return isTakeOrder;
    }

    @Override
    public void setТakeOrder() {
        super.isTakeOrder = true;

    }


}
