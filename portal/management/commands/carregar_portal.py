from django.core.management.base import BaseCommand
from portal.models import Conteudo, Menu

IMG = "/static/portal/img/"

CONTEUDOS = [
    ("Início", "inicio", """<section class="conteudo">
    <h1>Descrição do que você encontrará na página</h1>
    <article>
        <p>Aqui estão os currículos e os temas livres de José Kayky e Antonio Dias.</p>
        <p>Faça o uso dos botões do menu para navegar entre as páginas.</p>
    </article>
</section>"""),

    ("Currículo de Kayky", "curriculo-kayky", """<section class="conteudo">
    <h1>Currículo de José Kayky</h1>
    <article>
        <img class="imagem" src="%(img)sfoto_do_kayky.jpg" alt="Foto de José Kayky">
        <p>Nome: José Kayky</p>
        <p>Idade: 18 anos</p>
        <p>Cidade/Estado: Minha cidade / Meu estado</p>
        <p>Email: Email@aluno.ifal.edu.br</p>
        <p>Telefone: (XX) XXXXX-XXXX</p>
        <p>Formação: Instituto Federal de Alagoas</p>
        <p>Curso: Técnico em Informática</p>
        <p>Finalização prevista: 2026</p>
    </article>
    <article>
        <h2>Objetivo Profissional</h2>
        <p>Atuar na área da informática, adquirir experiência e desenvolver novas habilidades.</p>
    </article>
    <article>
        <h2>Habilidades</h2>
        <p>Ótima comunicação</p>
        <p>Trabalho em equipe</p>
        <p>Organização</p>
    </article>
</section>""" % {"img": IMG}),

    ("Tema Livre de Kayky", "tema-kayky", """<section class="conteudo">
    <h1>O Mentalista</h1>
    <article>
        <img class="imagem" src="%(img)smentalista_capa.jpg" alt="O Mentalista">
        <p>O Mentalista (The Mentalist) é uma série policial americana que foi ao ar entre 2008 e 2015, com 7 temporadas.</p>
        <p>A trama acompanha Patrick Jane, um ex-falso vidente que passa a trabalhar como consultor do CBI (Bureau de Investigação da Califórnia), usando técnicas de observação, leitura corporal e persuasão para resolver crimes ao lado de sua equipe.</p>
    </article>
    <article>
        <h2>Patrick Jane</h2>
        <p>Patrick Jane é o protagonista da série. Extremamente observador e manipulador, ele usa truques de mentalismo e raciocínio dedutivo para desvendar casos, sempre com um sorriso confiante no rosto.</p>
        <p>Ao longo da série, ele também busca vingança contra "Red John", um serial killer responsável pela morte de sua esposa e filha, o que dá à trama um tom mais sombrio por trás do humor leve dos episódios.</p>
    </article>
    <article>
        <h2>A equipe</h2>
        <p>A equipe de Patrick Jane é formada por personagens marcantes, como a agente Teresa Lisbon, Kimball Cho, Wayne Rigsby e Grace Van Pelt, cada um com uma personalidade própria que complementa o estilo investigativo pouco convencional de Jane.</p>
    </article>
</section>""" % {"img": IMG}),

    ("Currículo de Antonio", "curriculo-antonio", """<section class="conteudo">
    <h1>Currículo de Antonio Dias</h1>
    <article>
        <img class="imagem" src="%(img)sfoto_antonio.jpg" alt="Foto de Antonio">
        <p>Idade: 17 anos</p>
        <p>Cidade: Minha cidade</p>
        <p>Telefone: (XX) XXXXX-XXXX</p>
        <p>E-mail: Email@aluno.ifal.edu.br</p>
    </article>
    <article>
        <h2>Objetivo Profissional</h2>
        <p>Atuar na área da informática, adquirir experiência e desenvolver novas habilidades.</p>
    </article>
</section>""" % {"img": IMG}),

    ("Tema Livre de Antonio", "tema-antonio", """<section class="conteudo">
    <h1>Fisiculturismo: Renato Cariani</h1>
    <article>
        <img class="imagem" src="%(img)scariani.jpg" alt="Renato Cariani">
        <p>Renato Cariani é um fisiculturista brasileiro conhecido por competir na categoria Classic Physique, uma modalidade do fisiculturismo que valoriza um físico volumoso, porém com proporções mais estéticas e "clássicas" do que a categoria Open de bodybuilding.</p>
    </article>
    <article>
        <h2>O esporte</h2>
        <p>O fisiculturismo é um esporte que combina treino de musculação intenso, dieta rigorosa e, em nível competitivo, longos períodos de preparação para alcançar baixo percentual de gordura e alto volume muscular na época das competições.</p>
    </article>
    <article>
        <h2>Categorias</h2>
        <p>Além do Classic Physique, o fisiculturismo possui outras categorias, como Men's Physique, Bodybuilding (Open) e Bikini/Wellness (para atletas mulheres), cada uma com regras próprias sobre volume muscular, poses e estética exigida no palco.</p>
    </article>
</section>""" % {"img": IMG}),
]

# (título do menu, slug do conteúdo ou None, URL externa ou "")
MENU = [
    ("Início", "inicio", ""),
    ("CV de Kayky", "curriculo-kayky", ""),
    ("Tema Livre de Kayky", "tema-kayky", ""),
    ("CV de Antonio", "curriculo-antonio", ""),
    ("Tema Livre de Antonio", "tema-antonio", ""),
    ("GitHub", None, "https://github.com/Kaykyzin77/projeto-django-polls"),
    ("W3Schools", None, "https://www.w3schools.com/"),
]


class Command(BaseCommand):
    help = "Carrega os conteúdos e o menu da ATV06 no banco de dados"

    def handle(self, *args, **kwargs):
        Menu.objects.all().delete()
        for titulo, slug, html in CONTEUDOS:
            Conteudo.objects.update_or_create(
                slug=slug,
                defaults={"titulo": titulo, "conteudo_html": html, "ativo": True},
            )

        for ordem, (titulo, slug, url) in enumerate(MENU, start=1):
            if slug:
                Menu.objects.create(
                    titulo=titulo, tipo_destino=Menu.INTERNO, ordem=ordem,
                    ativo=True, conteudo=Conteudo.objects.get(slug=slug),
                )
            else:
                Menu.objects.create(
                    titulo=titulo, tipo_destino=Menu.EXTERNO, ordem=ordem,
                    ativo=True, url_externa=url,
                )
        self.stdout.write(self.style.SUCCESS("Portal carregado com sucesso!"))
