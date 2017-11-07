###############################################################################
# 1. ObjectFamilyInterface: common interface for genereated objects
# 2. FactoryObject: returns object
#
# Flow:
#           client ---> [Abstract Factory] <--- Concrete Factory #2 (Family 2)
#                               ^                           ^
#                               |                           |
#                       Concrete Factory #1 (Family 1)      |
#                               ^                           |
#                               |                   object2-1, object2-2,...
#                       object1-1, object1-2,...
###############################################################################
# Example: Food Can Factory

# 1. ObjectFamilyInterface
# abstract object classes
class MeatCanInterface(object):
    def m_label(self):
        pass
    
class FishCanInterface(object):
    def f_label(self):
        pass

class VegetableCanInterface(object):
    def v_label(self):
        pass

# concrete object classes
class PorkCan(MeatCanInterface):
    def m_label(self):
        print('[pork can\t$xx.x1]')

class BeefCan(MeatCanInterface):
    def m_label(self):
        print('[beef can\t$xx.x2]')

class SalmonCan(FishCanInterface):
    def f_label(self):
        print('[salmon can\t$xx.x3]')

class TunaCan(FishCanInterface):
    def f_label(self):
        print('[tuna can\t$xx.x4]')

class CornCan(VegetableCanInterface):
    def v_label(self):
        print('[corn can\t$xx.x5]')

class SpinachCan(VegetableCanInterface):
    def v_label(self):
        print('[spinach can\t$xx.x6]')

# 2. FactoryObject:
# abstract can factory
class CanFactoryInterface(object):
    def getCan(name):
        pass

# concrete can factory
class MeatCanFactory(CanFactoryInterface):
    @staticmethod
    def getCan(name):
        if name == 'pork':
            return PorkCan()
        elif name == 'beef':
            return BeefCan()
        else:
            assert 0, 'No %s can!' %name

class FishCanFactory(CanFactoryInterface):
    @staticmethod
    def getCan(name):
        if name == 'salmon':
            return SalmonCan()
        elif name == 'tuna':
            return TunaCan()
        else:
            assert 0, 'No %s can!' %name

class VegetableCanFactory(CanFactoryInterface):
    @staticmethod
    def getCan(name):
        if name == 'corn':
            return CornCan()
        elif name == 'spinach':
            return SpinachCan()
        else:
            assert 0, 'No %s can!' %name

if __name__ == '__main__':
    print('='*40)
    meat_can_factory = MeatCanFactory()
    meat_can_factory.getCan('beef').m_label()
    meat_can_factory.getCan('pork').m_label()
    print('='*40)
    fish_can_factory = FishCanFactory()
    fish_can_factory.getCan('salmon').f_label()
    fish_can_factory.getCan('tuna').f_label()
    print('='*40)
    veg_can_factory = VegetableCanFactory()
    veg_can_factory.getCan('corn').v_label()
    veg_can_factory.getCan('spinach').v_label()
    print('='*40)